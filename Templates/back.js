// 1. GET DATA (Fetch from API)
async function loadPatients() {
    const response = await fetch('/api/patients');
    const patients = await response.json();
    
    let tableBody = document.getElementById('patientTable');
    tableBody.innerHTML = ''; // Clear table
    
    patients.forEach(p => {
        tableBody.innerHTML += `
            <tr>
                <td>${p.patient_id}</td>
                <td>${p.name}</td>
                <td>${p.email}</td>
            </tr>`;
    });
}

// 2. POST DATA (Send to API)
async function submitPatient(event) {
    event.preventDefault();
    const patientData = {
        patient_id: document.getElementById('p_id').value,
        name: document.getElementById('p_name').value,
        dob: document.getElementById('p_dob').value,
        email: document.getElementById('p_email').value
    };

    const response = await fetch('/api/patients', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(patientData)
    });

    if (response.ok) {
        alert("Success!");
        loadPatients(); // Refresh the list automatically
    }
}