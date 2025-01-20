function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("closed");
}

document.addEventListener("DOMContentLoaded", () => {
    feather.replace();
});


function updateStatus(orderId, orderNumber) {
    fetch('/order-requests/update-status', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ order_id: orderId, order_number: orderNumber })
    }).then(res => res.json())
      .then(data => alert(data.message))
      .catch(err => console.error(err));
}

function addToTemp(orderId, orderNumber) {
    const temp = JSON.parse(localStorage.getItem('tempOrders') || '[]');
    temp.push({ order_id: orderId, order_number: orderNumber });
    localStorage.setItem('tempOrders', JSON.stringify(temp));
    alert("発注追加しました");
}