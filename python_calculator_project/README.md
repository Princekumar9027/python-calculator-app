
# Prince Advanced Scientific Calculator Project

## Features ✨

### Basic Operations
- ➕ Addition, Subtraction, Multiplication, Division
- 🔢 Decimal support
- ⚡ Real-time preview of calculations

### Logarithmic Functions 📊
- **log₁₀** - Logarithm base 10
- **ln** - Natural logarithm (base e)
- **logₓ** - Logarithm with custom base
- **Set Base** - Define custom logarithm base for repeated use

### Trigonometric Functions 📐
- **sin** - Sine (in degrees)
- **cos** - Cosine (in degrees)
- **tan** - Tangent (in degrees)

### Advanced Functions 🚀
- **√** - Square root
- **x²** - Power operator
- **n!** - Factorial
- **%** - Percentage

### UI Features
- 🌙 Dark Mode Interface
- 📜 Calculation History with SQLite Database
- 👁️ Real-time Result Preview
- 🎨 Color-coded buttons for different function types

## Installation & Run

### Step 1: Install Python
Make sure Python 3.7+ is installed

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Calculator
```bash
python main.py
```

## Usage Guide

1. **Basic Calculations**: Use number buttons and operators (+, -, *, /)
2. **Real-time Preview**: See results update as you type
3. **Logarithm with Custom Base**:
   - Click "logₓ" button
   - Enter your number
   - Dialog will ask for the base
   - Alternative: Click "Set Base" first to set a permanent base
4. **Trigonometric Functions**: Input angle in degrees, then click sin/cos/tan
5. **View History**: Click "Show History" button to see all past calculations

## Build Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Create EXE:

```bash
pyinstaller --onefile --windowed main.py
```

The executable will be in the `dist/` folder.

## Color Guide

- 🟢 Green = Equal button (calculate)
- 🔴 Red = Clear button
- 🔵 Blue = History
- 🟠 Orange = Logarithmic functions
- 🟦 Cyan = Trigonometric functions
- 🟫 Gray = Basic functions
