import pandas as pd

class DatabaseService:
    def __init__(self, csv_path='transaction.csv'):
        self.transactions = pd.read_csv(csv_path)

    def get_transactions(self, start_date, end_date, user_email):
        filtered_transactions = self.transactions[(self.transactions['user_email'] == user_email) &
                                                  (self.transactions['date_of_transaction'] >= start_date) &
                                                  (self.transactions['date_of_transaction'] <= end_date)]
        return filtered_transactions
