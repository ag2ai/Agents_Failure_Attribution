import re
import json
import os
import argparse

def read_predictions(eval_file):
    if not os.path.exists(eval_file):
        print(f"Error: Evaluation file not found at {eval_file}")
        return {}

    try:
        with open(eval_file, 'r', encoding='utf-8') as file:
            data = file.read()
    except Exception as e:
        print(f"Error reading evaluation file {eval_file}: {e}")
        return {}

    predictions = {}
    pattern = r"Prediction for ([^:]+\.json):(.*?)(?=Prediction for|\Z)"
    blocks = re.finditer(pattern, data, re.DOTALL)
    parsed_count = 0

    for block in blocks:
        content = block.group(2).strip()
        idx = block.group(1).strip()
        agent_name_match = re.search(r"Agent Name:\s*([\w_]+)", content, re.IGNORECASE)
        step_number_match = re.search(r"Step Number:\s*(\d+)", content, re.IGNORECASE)

        if agent_name_match and step_number_match:
            agent_name = agent_name_match.group(1)
            step_number = step_number_match.group(1)
            predictions[idx] = {
                'predicted_agent': agent_name,
                'predicted_step': f"{step_number}"
            }
            parsed_count += 1
        else:
            print(f"Warning: Could not parse Agent Name/Step Number for {idx} in {eval_file}")

    print(f"--- Predictions Read from {eval_file} ---")
    print(f"Successfully parsed predictions for {parsed_count} files.")
    print("=======================================")
    return predictions

def read_actual_data(labeled_json):
    try:
        with open(labeled_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        mistake_agent = data.get('mistake_agent')
        mistake_step = data.get('mistake_step')
        if mistake_agent is not None and mistake_step is not None:
            return str(mistake_agent), str(mistake_step)
        else:
            print(f"Warning: 'mistake_agent' or 'mistake_step' key missing in {labeled_json}")
            return None, None
    except FileNotFoundError:
        print(f"Error: Actual data file not found during read: {labeled_json}")
        return None, None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {labeled_json}")
        return None, None
    except Exception as e:
        print(f"Error reading actual data from {labeled_json}: {e}")
        return None, None

def evaluate_accuracy(predictions, data_path, total_files):
    correct_agent = 0
    correct_step = 0
    files_evaluated = 0

    if total_files == 0:
        print("Error: No JSON files found in the data path to evaluate against.")
        return 0.0, 0.0

    print(f"\n--- Starting Evaluation ---")
    print(f"Total reference JSON files found in {data_path}: {total_files}")
    print(f"Predictions available for {len(predictions)} files.")
    print("=======================================")

    for idx, pred in predictions.items():
        labeled_file = os.path.join(data_path, f"{idx}")

        if os.path.exists(labeled_file):
            files_evaluated += 1
            actual_agent, actual_step = read_actual_data(labeled_file)

            if actual_agent is not None and actual_step is not None:
                if actual_agent == pred['predicted_agent']:
                    correct_agent += 1
                if actual_step == pred['predicted_step']:
                    correct_step += 1
            else:
                 print(f"Skipping evaluation for {idx} due to issues reading actual data.")

        else:
            print(f"Warning: Labeled file not found for prediction key '{idx}': {labeled_file}")

    print("\n--- Evaluation Summary ---")
    print(f"Total reference files in data_path: {total_files}")
    print(f"Predictions parsed from eval file:  {len(predictions)}")
    print(f"Files evaluated (prediction found & actual data read): {files_evaluated}")
    print(f"Correct Agent Predictions: {correct_agent}")
    print(f"Correct Step Predictions:  {correct_step}")

    agent_accuracy = (correct_agent / total_files) * 100 if total_files > 0 else 0.0
    step_accuracy = (correct_step / total_files) * 100 if total_files > 0 else 0.0

    return agent_accuracy, step_accuracy

def main():
    parser = argparse.ArgumentParser(description="Evaluate agent and step prediction accuracy from an evaluation log file.")
    parser.add_argument(
        "--data_path",
        type=str,
        default='../Who&When/Algorithm-Generated',
        help="Path to the directory containing the ground truth files."
    )
    parser.add_argument(
        "--eval_file",
        type=str,
        required=True,
        help="Path to the evaluation log file containing the predictions."
    )
    args = parser.parse_args()
    
    data_path = args.data_path
    eval_file = args.eval_file

    if not os.path.isdir(data_path):
        print(f"Error: Data directory not found at {data_path}")
        actual_total_files = 0
    else:
        try:
            json_files_in_data_path = [
                f for f in os.listdir(data_path)
                if f.endswith('.json') and os.path.isfile(os.path.join(data_path, f))
            ]
            actual_total_files = len(json_files_in_data_path)
        except Exception as e:
            print(f"Error reading data directory {data_path}: {e}")
            actual_total_files = 0

    predictions = read_predictions(eval_file)

    agent_accuracy, step_accuracy = evaluate_accuracy(predictions, data_path, actual_total_files)

    print("\n--- Final Accuracy Results ---")
    print(f"Evaluation File: {eval_file}")
    print(f"Data Path:       {data_path}")
    print(f"Agent Accuracy: {agent_accuracy:.2f}%")
    print(f"Step Accuracy:  {step_accuracy:.2f}%")
    print(f"(Accuracy calculated based on {actual_total_files} total files in data path)")

if __name__ == "__main__":
    main()