# ML Code Reviewer 🔍

A comprehensive machine learning code analysis tool that automatically reviews Python ML code for best practices, potential issues, and optimization opportunities.

## Features ✨

- **🔍 Comprehensive Analysis**: Detects common ML pitfalls and anti-patterns
- **⚠️ Issue Detection**: Identifies critical errors, warnings, and suggestions
- **📊 Interactive Dashboard**: Clean, modern interface for viewing analysis results
- **🎯 ML-Specific Rules**: Specialized checks for ML workflows and algorithms
- **📈 Score Calculation**: Overall code quality scoring system
- **🚀 Real-time Processing**: Fast analysis with live progress feedback

## Architecture 🏗️

### Frontend (React + TypeScript)
- **Framework**: React 18 with TypeScript
- **Styling**: Tailwind CSS + shadcn/ui components
- **State Management**: TanStack Query for server state
- **File Upload**: React Dropzone for drag-and-drop functionality
- **UI Components**: Modern, responsive design with Lucide icons

### Backend (Node.js + Express)
- **Runtime**: Node.js with Express.js
- **Language**: TypeScript
- **File Processing**: Multer for file upload handling
- **Python Integration**: Child process spawning for ML analysis

### ML Analyzer (Python)
- **Code Analysis**: AST-based parsing and pattern matching
- **Rule Engine**: Comprehensive ML-specific rule sets
- **Issue Detection**: Multi-level severity classification
- **Report Generation**: Structured JSON output for frontend consumption

## Installation 🚀

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- npm or yarn

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI_powered_code_review_for_ML_pipelines
   ```

2. **Install frontend dependencies**
   ```bash
   cd client
   npm install
   ```

3. **Install backend dependencies**
   ```bash
   cd ../server
   npm install
   ```

4. **Install Python dependencies**
   ```bash
   cd ../ml_analyzer
   pip install -r requirements.txt
   ```

## Usage 💻

### Development Mode

1. **Start the backend server**
   ```bash
   cd server
   npm run dev
   ```
   Server will run on `http://localhost:5001`

2. **Start the frontend development server**
   ```bash
   cd client
   npm run dev
   ```
   Frontend will run on `http://localhost:5173`

3. **Access the application**
   Open your browser and navigate to `http://localhost:5173`

### Using the Application

1. **Upload Python File**: Drag and drop or click to select a `.py` file
2. **Start Analysis**: Click the "Start Analysis" button
3. **View Results**: Review the comprehensive analysis report with:
   - Overall quality score
   - Critical issues count
   - Warnings and suggestions
   - Line-specific feedback
   - Performance recommendations

## ML Analysis Rules 🧠

The analyzer checks for:

### Critical Issues
- **Syntax Errors**: Python syntax and import issues
- **Data Leakage**: Fitting scalers/transformers on full dataset
- **Missing Dependencies**: Undefined variables and imports

### Warnings
- **Feature Scaling**: Scale-sensitive algorithms without normalization
- **Random State**: Missing random_state parameters for reproducibility
- **Cross-validation Issues**: Improper CV setup and data splitting

### Suggestions
- **Code Quality**: PEP 8 compliance and best practices
- **Performance**: Optimization opportunities
- **ML Best Practices**: Industry-standard ML workflow recommendations

### Supported ML Libraries
- scikit-learn
- pandas
- numpy
- matplotlib/seaborn
- TensorFlow/Keras (basic support)
- PyTorch (basic support)

## Project Structure 📁

```
AI_powered_code_review_for_ML_pipelines/
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Main application pages
│   │   └── lib/          # Utility functions
│   └── package.json
├── server/                # Node.js backend
│   ├── src/
│   │   ├── api/          # Express route handlers
│   │   └── ml_analyzer/  # Python analysis scripts
│   └── package.json
├── ml_analyzer/           # Python ML analysis engine
│   ├── analyzer.py       # Main analysis logic
│   ├── main.py          # Entry point script
│   ├── rules.py         # ML-specific rule definitions
│   └── requirements.txt
└── README.md
```

## API Endpoints 🔗

### POST `/api/analysis`
Analyzes uploaded Python ML code file.

**Request**: 
- Method: POST
- Content-Type: multipart/form-data
- Body: Python file (.py)

**Response**:
```json
{
  "id": "unique-analysis-id",
  "projectName": "filename.py",
  "status": "completed",
  "overallScore": 85,
  "criticalIssues": 1,
  "warnings": 3,
  "performanceIssues": 0,
  "coverage": 95,
  "createdAt": "2025-07-26T12:00:00Z",
  "issues": [
    {
      "id": "issue-id",
      "severity": "warning",
      "title": "Feature Scaling",
      "description": "LogisticRegression is sensitive to feature scaling...",
      "lineStart": 15,
      "lineEnd": 15,
      "suggestions": "Consider using StandardScaler or MinMaxScaler..."
    }
  ]
}
```

## Development 🛠️

### Adding New Analysis Rules

1. **Define rules** in `ml_analyzer/rules.py`
2. **Implement detection logic** in `ml_analyzer/analyzer.py`
3. **Test with sample code** to ensure accuracy

### Frontend Development

- Uses TypeScript for type safety
- Tailwind CSS for styling
- Component-based architecture
- Real-time updates with TanStack Query

### Backend Development

- Express.js with TypeScript
- File upload handling with Multer
- Python process integration
- Error handling and logging

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Testing 🧪

### Sample Test File
```python
# test_ml_code.py
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# This will trigger scaling warnings
data = [[1, 2], [3, 4], [5, 6]]
labels = [0, 1, 0]

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
```

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Built with React, TypeScript, and Python
- UI components from shadcn/ui
- Icons from Lucide React
- Styling with Tailwind CSS

---

**Made with ❤️ for the ML community**