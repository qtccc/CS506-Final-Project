document.addEventListener('DOMContentLoaded', () => {
    const airportSelect = document.getElementById('airport');
    const result = document.getElementById('result');

    // Fetch airport codes and populate the dropdown
    fetch('/get_airports')
        .then(response => response.json())
        .then(data => {
            // console.log('Airports Data:', data); // Debugging
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
        const airport = airportSelect.value; // Correctly fetch the value
        const month = document.getElementById('month').value;

        // console.log('Selected Airport Value:', airport); // Debugging
        // console.log('Selected Month Value:', month); // Debugging

        fetch('/get_delays', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ airport, month })
        })
            .then(response => response.json())
            .then(data => {
                // console.log('Delay Data:', data); // Debugging
                if (data.error) {
                    result.textContent = `Error: ${data.error}`;
                } else {
                    const delayLikelihood = data.delay_likelihood !== null && data.delay_likelihood !== undefined
                        ? data.delay_likelihood.toFixed(2)
                        : 'N/A';
                    const weatherDelayLikelihood = data.weather_delay_likelihood !== null && data.weather_delay_likelihood !== undefined
                        ? data.weather_delay_likelihood.toFixed(2)
                        : 'N/A';

                    result.innerHTML = `
                        <p>Delay Likelihood: ${delayLikelihood} minutes</p>
                        <p>Weather Delay Likelihood: ${weatherDelayLikelihood} minutes</p>
                    `;
                }
            })
            .catch(error => {
                console.error('Error fetching delay data:', error);
                result.textContent = 'An error occurred while fetching delay data.';
            });
    });
});