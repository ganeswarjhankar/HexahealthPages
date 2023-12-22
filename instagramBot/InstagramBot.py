import boto3
import csv

def extract_table_from_pdf(pdf_path):
    # Initialize Amazon Textract client
    textract_client = boto3.client('textract')

    # Read PDF file as binary data
    with open(pdf_path, 'rb') as file:
        pdf_data = file.read()

    # Call Amazon Textract to analyze the document
    response = textract_client.analyze_document(Document={'Bytes': pdf_data})

    # Extract tables from the response
    tables = [item for item in response['Blocks'] if item['BlockType'] == 'TABLE']

    # Extract table data and write to CSV
    for idx, table in enumerate(tables):
        rows = []
        for relationship in table['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    child = next(item for item in response['Blocks'] if item['Id'] == child_id)
                    if child['BlockType'] == 'CELL':
                        rows.append(child['Text'])

        # Write table data to CSV
        with open(f'table_{idx + 1}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(rows)

# Example usage
pdf_path = 'D:\\invoice.pdf'
extract_table_from_pdf(pdf_path)
