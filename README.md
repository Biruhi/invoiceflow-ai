# 🧾 InvoiceFlow AI

🚀 **Live Demo**
https://invoiceflow-ai-5jqmejkwkphrglcrgttrkk.streamlit.app/

InvoiceFlow AI is an intelligent invoice processing platform built with Python and Streamlit. It automatically extracts structured information from PDF invoices, detects multiple invoices within a document, generates business analytics, and exports professional reports.

---

## 🚀 Features

### 📄 PDF Invoice Processing

Upload:

* Single Invoice PDFs
* Multi-page Invoice PDFs
* Multiple Invoice PDFs

Automatically extract:

* Invoice Number
* Vendor
* Customer
* Invoice Date
* Due Date
* Subtotal
* Tax
* Total Amount
* Currency

---

### 🔍 Multi-Invoice Detection

InvoiceFlow AI supports:

✅ One PDF → One Invoice

✅ Multiple PDFs → Multiple Invoices

✅ One PDF → Multiple Invoices

✅ Multiple Invoices on the Same Page

The system automatically identifies invoice boundaries and processes each invoice separately.

---

### 📊 Analytics Dashboard

Generate business insights including:

* Invoice Count
* Vendor Analysis
* Customer Analysis
* Average Invoice Value
* Total Spend
* Tax Analysis

---

### 📈 Vendor Spend Analytics

Visualize:

* Spend by Vendor
* Vendor Distribution
* Invoice Volume by Vendor

---

### 🏢 Invoice Details Dashboard

View:

* Invoice Information
* Vendor Details
* Customer Details
* Financial Summary

---

### 📤 Export Options

Export extracted invoice records to:

* Excel (XLSX)

---

## 📂 Sample Invoice Files

The repository includes sample invoice files for testing.

### Included Samples

* `sample_invoice_INV-2026-001.pdf`
* `sample_invoice_INV-2026-045.pdf`
* `multi_invoice_same_page_sample.pdf`
* `sample_invoice_missing_fields.pdf`
* `sample_invoice_enterprise.pdf`

These files demonstrate:

* Standard invoices
* Different vendor formats
* Multi-invoice documents
* Missing field scenarios
* Enterprise-scale invoices

---

## 📊 Supported Invoice Fields

InvoiceFlow AI extracts:

```text
Invoice Number
Vendor
Customer
Invoice Date
Due Date
Subtotal
Tax
Total
Currency
```

---

## 🛠 Technology Stack

* Python
* Streamlit
* Pandas
* Plotly
* PyMuPDF
* OpenPyXL

---

## 📁 Project Structure

```text
invoiceflow-ai/

├── app/
│   ├── analytics.py
│   ├── exporter.py
│   ├── extractor.py
│   ├── invoice_detector.py
│   ├── logger.py
│   ├── parser.py
│   └── __init__.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── sample_data/
│   ├── sample_invoice_INV-2026-001.pdf
│   ├── sample_invoice_INV-2026-045.pdf
│   ├── multi_invoice_same_page_sample.pdf
│   ├── sample_invoice_missing_fields.pdf
│   └── sample_invoice_enterprise.pdf
│
├── outputs/
├── logs/
│
├── requirements.txt
├── main.py
└── .gitignore
```

---

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run dashboard/streamlit_app.py
```

---

## 📈 Key Capabilities

* PDF Processing
* Invoice Extraction
* Multi-Invoice Detection
* Vendor Analytics
* Financial Reporting
* Business Intelligence
* Report Exporting

---

## 🎯 Business Use Cases

* Accounts Payable Automation
* Invoice Processing
* Vendor Spend Tracking
* Financial Reporting
* Invoice Analytics
* Document Automation

---

## 🔮 Future Enhancements

* OCR Support for Scanned PDFs
* AI Invoice Classification
* Database Integration
* Automated Approval Workflows
* Email Invoice Processing
* Multi-Currency Analytics

---

## 👨‍💻 Author

**Biruhi Tesfaye Abeje**

Built as a portfolio project showcasing:

* Python Development
* PDF Processing
* Data Extraction
* Business Intelligence
* Streamlit Applications
* Analytics Dashboard Development
* Document Automation
