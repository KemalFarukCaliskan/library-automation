# Library Management System with Tkinter GUI

A standalone, modern desktop application built with Python to automate library cataloging, book borrowing tracking, and genre-based inventory management. The project directly applies robust Object-Oriented Programming (OOP) paradigms coupled with structural event-driven GUI layouts.

## 🚀 Key Features
- **Object-Oriented Architecture:** Implements a clean class hierarchy with class inheritance (`Kitap` inheriting from `Yayin`) and dynamic polymorphism attributes.
- **Smart Cataloging & Aggregation:** Automatically groups and lists library items dynamically based on their specific genres (Tür).
- **State & Transaction Pipeline:** Features real-time book status handling ("Mevcut" / "Ödünç Verildi") ensuring logical criteria protection to avoid duplicate loan errors.
- **Modern UI Look (Tkinter 'clam'):** Leverages advanced `ttk` themes and stylized components, creating secondary popup dialog layers, data input structures, and dynamic scrollable text windows.

---

## 📁 Repository Structure
- `library.py`: Unified code infrastructure running the underlying logical backend algorithms alongside the complete structural Tkinter engine framework.

---

## 🛠️ Software Architecture Deep Dive

### 1. Data Models & Inheritance Diagram
- **Base Class (`Yayin`):** Establishes common criteria variables such as titles (`baslik`), publication years (`yayin_yili`), and systemic availability flags (`durum`).
- **Derived Class (`Kitap`):** Extends the base entity via `super().__init__()` and encapsulates domain-specific fields including author records (`yazar`), `isbn` entries, and genre types (`tur`).

### 2. Operational Controller Workflow
- **`kitap_ekle`:** Appends new operational instances into a dynamic collection list backend.
- **`kitaplari_listele`:** Builds nested dictionaries to map collections by category blocks, providing distinct sorting structures before pushing updates into active interface panels.
- **`odunc_ver`:** Processes structural loan actions via case-insensitive lookup conditions, protecting book asset states dynamically.

---

## 💻 Tech Stack
- **Language:** Python
- **Libraries:** Tkinter, ScrolledText, Messagebox, Simpledialog, TTK Styling System
- **Concepts:** Inheritance, Super Initializers, Encapsulation, State Tracking, Event Handling Loops

---

## ⚙️ How to Run
Execute the unified python file using standard execution protocols:
```bash
python library.py
