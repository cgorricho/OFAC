# Quick Start Guide - Running the OFAC Screening Tool

This guide will help you quickly get the OFAC Sanctions Screening Tool up and running for testing.

---

## Prerequisites

- Python 3.11+ installed
- Virtual environment activated (`.venv` should exist)
- Internet connection (for downloading OFAC data if needed)

---

## Step 1: Activate Virtual Environment

```bash
cd /home/cgorricho/apps/OFAC
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt.

---

## Step 2: Check OFAC Data

The app requires OFAC data files to function. Check if data exists:

```bash
ls -la data/
```

**If data directory is empty or missing files:**

You'll need to download OFAC data. The app can do this automatically, or you can use the updater:

```bash
# Option 1: Let the app download on first run (it will prompt)
# Option 2: Use the Python updater directly
python -c "from ofac.data.updater import OFACUpdater; updater = OFACUpdater(); updater.download_sdn_files()"
```

**Required files:**
- `data/sdn.csv`
- `data/alt.csv`
- `data/add.csv`

---

## Step 3: Run the Application

### Option A: Streamlit Web App (Recommended for Testing)

The easiest way to test the full functionality:

```bash
# Method 1: Using the project's main entry point
python -m ofac --streamlit

# Method 2: Direct Streamlit command
streamlit run src/ofac/streamlit/app.py
```

The app will:
- Start on `http://localhost:8501` (default Streamlit port)
- Automatically open in your browser
- Load OFAC data on startup
- Show the main screening interface

**What you'll see:**
1. Header with OFAC data freshness indicator
2. File upload area (drag-drop CSV/Excel files)
3. Column mapping interface
4. Screening execution with progress
5. Results display with filtering
6. Export button for Excel reports

### Option B: FastAPI Backend Only

To test the API endpoints:

```bash
# Method 1: Using the project's main entry point
python -m ofac --api

# Method 2: Direct uvicorn command
uvicorn ofac.api.main:app --reload
```

The API will:
- Start on `http://localhost:8000` (default)
- Provide OpenAPI docs at `http://localhost:8000/docs`
- Health check at `http://localhost:8000/health`

**Test the API:**
```bash
# Health check
curl http://localhost:8000/health

# Data status
curl http://localhost:8000/data/status

# Single entity screening
curl -X POST http://localhost:8000/screenings/single \
  -H "Content-Type: application/json" \
  -d '{"entity_name": "Test Organization", "country": "US"}'
```

---

## Step 4: Test with Sample Data

### Create a Test CSV File

Create a file `test_entities.csv`:

```csv
Organization Name,Country,Description
ACME Corporation,US,Technology company
Archdiocese of Bangui,CF,Religious organization
Syrian Development Foundation,SY,Humanitarian aid project
Test Organization,GB,General purpose
```

### Upload and Screen

1. Open the Streamlit app (http://localhost:8501)
2. Click "Upload File" or drag-drop your CSV
3. The app will auto-detect columns
4. Click "Start Screening"
5. View results with color-coded status
6. Expand match details for REVIEW/NOK cases
7. Download Excel report

---

## Troubleshooting

### Issue: "OFAC data files not found"

**Solution:**
```bash
# Download OFAC data
python -c "from ofac.data.updater import OFACUpdater; updater = OFACUpdater(); updater.download_sdn_files()"
```

### Issue: "Module not found" errors

**Solution:**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Reinstall dependencies
uv sync
```

### Issue: Port already in use

**Solution:**
```bash
# Use a different port
python -m ofac --streamlit --port 8502
# or
uvicorn ofac.api.main:app --port 8001
```

### Issue: API not accessible from Streamlit

**Solution:**
- Ensure FastAPI is running on port 8000 (default)
- Check `OFAC_API_HOST` and `OFAC_API_PORT` in `.env` or environment variables
- Default: `127.0.0.1:8000`

---

## Configuration

### Environment Variables

Create a `.env` file (or copy from `.env.example`):

```bash
# OFAC Data Path (default: ./data)
OFAC_DATA_PATH=./data

# API Configuration (for Streamlit to connect to FastAPI)
OFAC_API_HOST=127.0.0.1
OFAC_API_PORT=8000

# Matching Thresholds
OFAC_MATCH_THRESHOLD_NOK=95
OFAC_MATCH_THRESHOLD_REVIEW=80

# Logging
OFAC_LOG_LEVEL=INFO
```

---

## Quick Test Checklist

- [ ] Virtual environment activated
- [ ] OFAC data files exist (`data/sdn.csv`, `data/alt.csv`, `data/add.csv`)
- [ ] Streamlit app starts without errors
- [ ] Can upload a test CSV file
- [ ] Screening executes successfully
- [ ] Results display correctly
- [ ] Can download Excel report
- [ ] Freshness indicator shows data age
- [ ] Can trigger data update (if needed)

---

## Next Steps

1. **Test with Real Data:** Use actual organization names from your projects
2. **Review Results:** Check that OK/REVIEW/NOK classifications make sense
3. **Test Exception Review:** Try the analyst notes and decision tracking
4. **Test Data Updates:** Use the update button to refresh OFAC data
5. **Review Reports:** Check that Excel reports have all required fields

---

## Support

If you encounter issues:
1. Check the logs in the terminal
2. Review error messages in the Streamlit app
3. Check that all dependencies are installed
4. Verify OFAC data files are present and valid

---

**Happy Testing!** 🚀

