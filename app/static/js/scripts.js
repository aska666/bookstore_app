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

const salesData = {
    labels: ['本', 'CD', 'DVD', '文房具', 'その他'],
    datasets: [{
        label: '売上',
        data: [120000, 50000, 30000, 20000, 10000],
        backgroundColor: ['#FF6B6B', '#4C9C4A', '#FFCE56', '#36A2EB', '#FF9F40'],
        borderColor: ['#FF6B6B', '#4C9C4A', '#FFCE56', '#36A2EB', '#FF9F40'],
        borderWidth: 1
    }]
};

const salesConfig = {
    type: 'pie',
    data: salesData,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        return `${tooltipItem.label}: ¥${tooltipItem.raw.toLocaleString()}`;
                    }
                }
            }
        }
    }
};

const salesChart = new Chart(document.getElementById('salesChart'), salesConfig);




document.addEventListener('DOMContentLoaded', function() {
    const warehouseNames = ['倉庫A', '倉庫B', '倉庫C', '店舗1', '店舗2'];
    const shippingDays = ["明日", "配送中", "1週間以内", "1か月程度"];
    const warehouseDaysTable = document.getElementById('warehouse-days');

    const bookNameInput = document.getElementById('book-name');
    const bookList = document.getElementById('book-list');
    const isbnInput = document.getElementById('isbn');
    const publisherInput = document.getElementById('publisher');

    const GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes?q=";

    bookNameInput.addEventListener('input', function() {
        const query = bookNameInput.value.trim();

        if (query.length > 0) {
            fetchBooks(query);
        } else {
            bookList.innerHTML = '';
            bookList.style.display = 'none';
        }
    });

    function fetchBooks(query) {
        const url = `${GOOGLE_BOOKS_API_URL}${encodeURIComponent(query)}&maxResults=5`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                const books = data.items || [];
                displayBookSuggestions(books);
            })
            .catch(error => {
                console.error('Error fetching books:', error);
                bookList.innerHTML = '<li>予測候補の取得に失敗しました。</li>';
                bookList.style.display = 'block';
            });
    }

    function displayBookSuggestions(books) {
        bookList.innerHTML = '';

        if (books.length === 0) {
            bookList.innerHTML = '<li>書籍が見つかりませんでした。</li>';
        } else {
            books.forEach(book => {
                const li = document.createElement('li');
                li.classList.add('cursor-pointer', 'hover:bg-gray-200', 'p-2');
                li.textContent = book.volumeInfo.title;

                li.addEventListener('click', function() {
                    bookNameInput.value = book.volumeInfo.title;
                    isbnInput.value = book.volumeInfo.industryIdentifiers ? book.volumeInfo.industryIdentifiers[0].identifier : '情報なし';
                    publisherInput.value = book.volumeInfo.publisher || '情報なし';
                    bookList.innerHTML = '';
                    bookList.style.display = 'none';

                    populateWarehouseTable();
                });

                bookList.appendChild(li);
            });
        }

        bookList.style.display = books.length > 0 ? 'block' : 'none';
    }

    document.addEventListener('DOMContentLoaded', function() {
        const warehouseNames = ['倉庫A', '倉庫B', '倉庫C', '倉庫D'];
        const shippingDays = ["明日", "配送中", "1週間以内", "1か月程度"];
        const costs = ["¥500", "¥1000", "¥1500", "¥2000", "¥2500"];
        const warehouseDaysTable = document.getElementById('warehouse-days');
    
        function populateWarehouseTable() {
            warehouseDaysTable.innerHTML = '';
    
            for (let i = 0; i < 5; i++) {
                const randomWarehouse = warehouseNames[i];
                const randomShippingDay = shippingDays[Math.floor(Math.random() * shippingDays.length)];
                const randomCost = costs[Math.floor(Math.random() * costs.length)];
    
                const radioId = `radio-${i}`;
    
                const row = document.createElement('tr');
                row.classList.add('border-b', 'border-gray-300');
    
                row.innerHTML = `
                    <td class="px-4 py-2 border border-gray-300">${randomWarehouse}</td>
                    <td class="px-4 py-2 border border-gray-300">${randomShippingDay}</td>
                    <td class="px-4 py-2 border border-gray-300">${randomCost}</td>
                    <td class="px-4 py-2 border border-gray-300">
                        <input type="radio" name="warehouse" id="${radioId}" value="${randomWarehouse}:${randomShippingDay}:${randomCost}">
                    </td>
                `;
                warehouseDaysTable.appendChild(row);
            }
        }
        populateWarehouseTable();
    })});
