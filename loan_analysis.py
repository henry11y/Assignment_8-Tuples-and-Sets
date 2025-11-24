
# ...existing code...
import csv
import os
import sys

def detect_columns(header):
    age_idx = reason_idx = None
    for i, h in enumerate(header):
        h_l = h.strip().lower()
        if age_idx is None and 'age' in h_l:
            age_idx = i
        if reason_idx is None and ('reason' in h_l or 'purpose' in h_l or 'loan' in h_l):
            reason_idx = i
    return age_idx, reason_idx

def top_two_reasons_by_age(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return

    age_ranges = set()
    counts_by_age = {}  # age -> { reason -> count }

    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            print("Input CSV is empty.")
            return

        age_idx, reason_idx = detect_columns(header)
        if age_idx is None or reason_idx is None:
            # ask user to provide column names if detection failed
            print("Could not auto-detect 'age' and/or 'reason' columns from header:")
            print(header)
            age_name = input("Enter the exact column name for age range: ").strip()
            reason_name = input("Enter the exact column name for loan reason: ").strip()
            try:
                age_idx = header.index(age_name)
                reason_idx = header.index(reason_name)
            except ValueError:
                print("Provided column names not found in header. Exiting.")
                return

        for row in reader:
            # guard against short rows
            if max(age_idx, reason_idx) >= len(row):
                continue
            age = row[age_idx].strip()
            reason = row[reason_idx].strip()
            if not age:
                continue
            age_ranges.add(age)
            if age not in counts_by_age:
                counts_by_age[age] = {}
            if reason:
                counts_by_age[age][reason] = counts_by_age[age].get(reason, 0) + 1

    # build tuples (age_range, top_reason_1, top_reason_2)
    result_tuples = []
    for age in sorted(age_ranges):
        reason_counts = counts_by_age.get(age, {})
        # sort by count desc, then reason asc for deterministic tie-break
        sorted_reasons = sorted(reason_counts.items(), key=lambda x: (-x[1], x[0]))
        top1 = sorted_reasons[0][0] if len(sorted_reasons) >= 1 else ''
        top2 = sorted_reasons[1][0] if len(sorted_reasons) >= 2 else ''
        result_tuples.append((age, top1, top2))

    # write output CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['age_range', 'top_reason_1', 'top_reason_2'])
        for t in result_tuples:
            writer.writerow(t)

    print(f"Wrote {len(result_tuples)} rows to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        infile = sys.argv[1]
    else:
        infile = input("Path to loans CSV file: ").strip()
    outfile = os.path.splitext(infile)[0] + '_top_reasons_by_age.csv'
    top_two_reasons_by_age(infile, outfile)
# ...existing code...