import csv
import os
import os.path
import datetime


class Srs:
    stats_file = None
    stats = {}
    field_names = ['file', 'success_count', 'due_date']

    # SRS programs often adjust intervals based on user performance / ease of recall,
    # but since I don't want to pause after every phrase, in Julius they will always stay the same.
    srs_intervals = [1, 2, 4, 7, 11, 14, 21, 35, 70, 105]

    def __init__(self, directory):
        if not os.path.isdir(directory):
            raise ValueError('Cannot save SRS stats to path {0} as it is not a directory'.format(directory))

        julius_dir = os.path.join(directory, '.julius')
        os.makedirs(julius_dir, exist_ok=True)
        self.stats_file = os.path.join(julius_dir, 'stats.csv')

        existing_files = self.get_files(directory)

        if os.path.exists(self.stats_file):
            self.read_stats(existing_files)

        # add default file stat row for any files that exist in the directory but are not covered by stats
        self.stats.update(dict([[f, self.default_stat(f)] for f in existing_files if f not in self.stats.keys()]))

    def __del__(self):
        self.save_stats()

    @staticmethod
    def get_files(directory):
        """Return all files in a given directory"""
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    @staticmethod
    def default_stat(file):
        """Return a default file stat row"""
        return {'file': file, 'success_count': 0, 'due_date': datetime.date.today().isoformat()}

    @staticmethod
    def next_date_due(prev_date_due, success_count):
        """Return the next date the file is due to be repeated"""
        return prev_date_due + datetime.timedelta(days=Srs.srs_intervals[success_count])

    def read_stats(self, files):
        """Load stats for specified files from the stats file"""
        with open(self.stats_file, newline='', encoding='utf-8') as fp:
            reader = csv.DictReader(fp)
            self.stats = {row['file']: row for row in reader if row['file'] in files}

    def save_stats(self):
        """Save stats to the stats file"""
        with open(self.stats_file, 'w', newline='', encoding='utf-8') as fp:
            writer = csv.DictWriter(fp, fieldnames=self.field_names)
            writer.writeheader()
            for row in self.stats.values():
                writer.writerow(row)
