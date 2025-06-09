
# 🧠 YellowPages Lead Generator

A lightweight, user-friendly web tool to generate business leads from YellowPages using keyword and location-based search. Built as part of the Caprae Capital AI-Readiness Pre-Screening Challenge.

## 🚀 Features

- 🔍 Scrapes business names, phone numbers, and addresses from YellowPages
- ✅ Removes duplicate entries
- 🌍 Location + keyword based search
- 🧭 Paginated scraping (up to 5 pages)
- 💾 Download results as CSV
- 🖥️ Clean, intuitive Streamlit interface
- 🛡️ Uses `undetected_chromedriver` to bypass anti-bot measures

## 📦 Tech Stack

- **Python**
- **Selenium + undetected-chromedriver**
- **Pandas**
- **Streamlit**

## 📁 Project Structure

```
├── LeadGenTool.py     # Core scraping logic
├── app.py             # Streamlit web interface
├── README.md          # Project overview (this file)
└── requirements.txt   # Python dependencies (optional)
```

## 🧪 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/your-username/yellowpages-leadgen.git
cd yellowpages-leadgen
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**
```bash
streamlit run app.py
```

## ⚙️ Dependencies

Add this to your `requirements.txt`:

```
pandas
streamlit
undetected-chromedriver
selenium
```

## 📷 Screenshots

> 📌 Include a few screenshots of the UI showing:
> - Input form
> - Scraped data table
> - CSV download button

## 📌 Limitations

- Only scrapes publicly available YellowPages data
- No email or website scraping yet (future enhancement)
- Captcha or IP bans may occur with heavy usage

## 🤖 Future Improvements

- Email/website scraping
- Lead scoring and categorization
- CRM export integration (HubSpot, Zoho)
- Docker containerization

## 📄 License

MIT License

## 🙋‍♂️ Author

Created by [Your Name] for the Caprae Capital Pre-Internship AI Challenge.
