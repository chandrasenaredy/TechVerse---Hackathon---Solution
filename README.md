# Patient Appointmnet Booking Assistant #

A lightweight, full-stack **Hospital Management Web Application** built with **Flask** and **MySQL**. All HTML is embedded in a single Python file — no external templates needed. Run it with one command and open it in your browser.

---

## Features

### Patient Management
- Register patients with ID, name, date of birth, email, phone, pincode, and location
- View all registered patients in a table
- Delete patient records
- Email validation (must contain `@`)

### Appointment Booking
- Book appointments by selecting a patient, doctor, date, and time
- Auto-fills doctor specialty on selection
- Captures pincode and location for each appointment
- **30-minute conflict check** — blocks double-booking within the same time window
- **Doctor leave check** — prevents booking on a doctor's approved leave day with a popup
- Update appointment status: Scheduled / Completed / Cancelled
- Filter appointments by status and delete them

### Doctor Management
- Add doctors with ID, name, specialty, email, and phone
- **Auto-increment Doctor ID** — leave blank and it generates `D001`, `D002`, ... automatically
- View all doctors on record

### Doctor Leave Management
- Mark single-day or date-range leaves for any doctor
- Add a reason for each leave
- Visual **monthly leave calendar** per doctor with month navigation
- View and remove leave records
- Appointment booking is automatically blocked on leave days

### Service Requests
- Submit internal service/maintenance requests with a title and description
- Track status: Pending → In Progress → Resolved

---

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/hcl-hospital-management.git
cd hcl-hospital-management
```

**2. Install dependencies**

```bash
pip install flask mysql-connector-python
```

**3. Set up the MySQL database**

```sql
CREATE DATABASE hcl;
```

**4. Configure the database connection**

Open `app.py` and update the `DB` config at the top:

```python
DB = {
    "host":     "localhost",
    "user":     "root",
    "password": "your_password",
    "database": "hcl"
}
```

**5. Run the app**

```bash
python app.py
```

**6. Open in browser**

```
http://127.0.0.1:5000
```

The app will **automatically create all required tables** on first run — no manual SQL setup needed.

---

## Database Schema

| Table | Description |
|---|---|
| `patients` | Patient records with contact and location info |
| `doctors` | Doctor profiles with specialty |
| `appointments` | Bookings linking patients and doctors |
| `doctor_leaves` | Leave days per doctor |
| `service_requests` | Internal maintenance/service tickets |

---

## Project Structure

```
hcl-hospital-management/
|
|-- app.py        # Main application — all routes, APIs, and HTML in one file
|-- hcl.db        # SQLite DB (reference / dev use)
|-- README.md
```

---

## API Endpoints

### Patients
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/patients` | List all patients |
| POST | `/api/patients` | Register a new patient |
| DELETE | `/api/patients/<id>` | Delete a patient |

### Doctors
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/doctors` | List all doctors |
| POST | `/api/doctors` | Add a doctor (ID auto-generated if blank) |

### Appointments
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/appointments` | List all appointments |
| POST | `/api/appointments` | Book an appointment |
| PUT | `/api/appointments/<id>` | Update appointment status |
| DELETE | `/api/appointments/<id>` | Delete an appointment |

### Doctor Leaves
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/doctor-leaves` | List leaves (filter by `?doctor_id=`) |
| POST | `/api/doctor-leaves` | Mark a leave day |
| DELETE | `/api/doctor-leaves/<id>` | Remove a leave day |
| GET | `/api/doctor-leaves/check` | Check if doctor is on leave on a date |

### Service Requests
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/service-requests` | List all requests |
| POST | `/api/service-requests` | Create a new request |
| PUT | `/api/service-requests/<id>` | Update request status |

### Debug
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/debug` | Check DB connection and table row counts |

---

## Validation and Error Handling

- **Email** — must contain `@`
- **Doctor ID** — auto-increments if left blank (`D001`, `D002`, ...)
- **Appointment conflict** — HTTP `409` returned if doctor has a booking within 30 minutes of the requested slot; popup shown in UI
- **Doctor on leave** — HTTP `423` returned if doctor has an approved leave on the selected date; popup shown in UI
- All errors surface as toast notifications in the UI and JSON error responses from the API

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | MySQL via mysql-connector-python |
| Frontend | HTML, CSS, JavaScript (embedded in Flask) |
| Fonts | Google Fonts — DM Serif Display, DM Sans |

---

## Pages

| Route | Page |
|---|---|
| `/` | Patient Management |
| `/appointments` | Appointment Booking and Doctors |
| `/leave-management` | Doctor Leave Management |
| `/service-requests` | Service Requests |

---

## License

This project was built as part of the **HCL Hackathon**. Feel free to use and extend it.
