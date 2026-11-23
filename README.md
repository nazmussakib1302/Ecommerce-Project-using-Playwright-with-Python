Step 1: Set up the environment

mkdir playwright-python-framework && cd playwright-python-framework

python -m venv venv                  # create a virtual environment
source venv/bin/activate             # Windows: venv\Scripts\activate

pip install pytest-playwright pytest-html pytest-xdist python-dotenv
playwright install                   # downloads Chromium, Firefox, WebKit

pip freeze > requirements.txt        # save exact versions

Step 2: Project structure (files and folders required)
│
├── .github/
│   └── workflows/
│       └── playwright.yml        # CI/CD pipeline (GitHub Actions)
│
├── config/
│   ├── __init__.py
│   └── config.py                 # reads environment settings (.env)
│
├── pages/                        # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py              # common methods used by all pages
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/                        # test cases only
│   ├── __init__.py
│   ├── conftest.py               # (optional) fixtures only for tests/
│   ├── test_login.py
│   └── test_dashboard.py
│
├── test_data/
│   └── login_data.json           # test inputs (users, invalid inputs, etc.)
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py                # random data, date formatting, etc.
│   └── logger.py                 # logging setup
│
├── reports/                      # HTML reports (generated, not committed)
├── test-results/                 # screenshots, videos, traces (generated)
│
├── conftest.py                   # global fixtures and hooks
├── pytest.ini                    # pytest configuration
├── requirements.txt              # dependencies
├── .env                          # secrets and env values (NOT committed)
├── .env.example                  # template of .env (committed)
├── .gitignore
└── README.md                     # how to set up and run the project