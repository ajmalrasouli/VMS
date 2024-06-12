document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/visitors/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#visitorTable tbody');
            tableBody.innerHTML = '';
            data.forEach(visitor => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${new Date(visitor.sign_in_time).toLocaleString()}</td>
                    <td>${visitor.first_name}</td>
                    <td>${visitor.last_name}</td>
                    <td>${visitor.visitor_type}</td>
                    <td>
                        ${visitor.is_signed_out ? 'Signed Out' : `<button onclick="signOut(${visitor.id})">Sign Out</button>`}
                    </td>
                `;
                tableBody.appendChild(row);
            });
        });
});

function signOut(visitorId) {
    fetch(`/api/visitors/signout/${visitorId}/`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                location.reload();
            }
        });
}
