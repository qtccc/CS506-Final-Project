document.addEventListener('DOMContentLoaded', () => {
    const airportSelect = document.getElementById('airport');
    const result = document.getElementById('result');


    // Fetch airport codes and populate the dropdown
    fetch('/get_airports')
        .then(response => response.json())
        .then(data => {
            data.forEach(airport => {
                const option = document.createElement('option');
                option.value = airport.code;
                option.textContent = `${airport.code} - ${airport.name}`;
                airportSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching airports:', error));

    // Handle form submission
    document.getElementById('submit').addEventListener('click', () => {
        const airport = airportSelect.value;
        const month = document.getElementById('month').value;

        fetch('/get_delays', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ airport, month })
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    result.textContent = `Error: ${data.error}`;
                } else {
                    result.textContent = `Delay Likelihood: ${data.delay_likelihood.toFixed(2)} minutes`;
                }
            });
    });
});