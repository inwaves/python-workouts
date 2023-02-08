def passwd_to_csv(in_file: str, out_file: str) -> None:
    import csv
    creds = {}
    try:
        with open(in_file, encoding="utf-8") as fileobj:
            for line in fileobj:
                if not line.startswith("#") and ":" in line:
                    elems = line.split(":")
                    creds[elems[0].strip()] = int(creds[2].strip())
                continue
    except Exception as e:
        print(e)

    try:
        with open(out_file, "w", encoding="utf-8") as file_writer:
            csv_writer = csv.writer(file_writer)
            for k, v in creds.items():
                csv_writer.writerow(f"{k}\t{v}")
    except Exception as e:
        print(e)
