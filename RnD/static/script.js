var side_bar = document.querySelector(".side-bar");
var ham = document.querySelector(".ham p");
var closes = document.getElementById("close");

ham.addEventListener("click", ()=>{
    side_bar.classList.toggle("show-side");
});

closes.addEventListener("click", ()=>{
    side_bar.classList.toggle("show-side");
});

var nav1 = document.querySelector(".navbar1");
var val;
window.onscroll = function(){
    if(document.documentElement.scrollTop > 20){
        nav1.classList.add("sticky");
    }
    else{
        nav1.classList.remove("sticky");
    }
}


// const tablesData = {};

//     // Initialize tablesData with 2D array of 0 values for each table ID
//     document.addEventListener('DOMContentLoaded', function () {
//         initializeTableValues();
//         const tableIds = document.querySelectorAll('table[id^="table"]');
//         tableIds.forEach(function (table) {
//             const tableId = table.id;
//             tablesData[tableId] = initializeTableData(table);
//             // {% comment %} calculateAndDisplayTotalExpenses(tableId);
//             // calculateAndDisplayClosingBalance(tableId); {% endcomment %}
//         });

//         // Your existing DOMContentLoaded code (if any)
//     });

//     function initializeTableData(table) {
//         const inputFields = table.querySelectorAll('input[type="number"]');
//         const tableData = {};

//         inputFields.forEach(function (input) {
//             tableData[input.name] = 0;
//         });

//         return tableData;
//     }

//     function initializeTableValues() {
//         const inputFields = document.querySelectorAll('input[type="number"]');
//         inputFields.forEach(function (input) {
//             input.value = 0;
//         });
//     }

//     function updateTable(tableId) {
//         var tableData = getTableData(tableId);
//         tablesData[tableId] = tableData;

//         // Implement the logic to update the table with the retrieved data
//         calculateAndDisplayTotalAmount(tableId);
//         calculateAndDisplayTotalExpenses(tableId);
//         calculateAndDisplayClosingBalance(tableId);
//          tableData = getTableData(tableId);
//         tablesData[tableId] = tableData;
//         // console.log(tableId);
//          console.log(tablesData);
//          console.log(JSON.stringify(tableData));
//          var fellowshipNo = "{{ fellowship_no }}";
//         saveTableDataToDjango(tablesData,fellowshipNo);
//      //   alert(`Table ${tableId} updated: ${JSON.stringify(tableData)}`);
//     }

//     function getTableData(tableId) {
//         const table = document.querySelector(`#${tableId}`);
//         const inputFields = table.querySelectorAll('input[type="number"]');
//         const tableData = {};

//         inputFields.forEach(function (input) {
//             tableData[input.name] = input.value;
//         });

//         return tableData;
//     }
//     function calculateAndDisplayTotalExpenses(tableId) {
//         const table = document.querySelector(`#${tableId}`);
//         const rows = table.querySelectorAll('tr:not(.header-row)');

//         rows.forEach(function (row) {
//             const inputFields = row.querySelectorAll('input[type="number"]');
//             let totalExpenses = 0;

//             inputFields.forEach(function (input) {
//                 if (input.name.endsWith('_Apr') || input.name.endsWith('_May') || input.name.endsWith('_Jun') ||
//                     input.name.endsWith('_Jul') || input.name.endsWith('_Aug') || input.name.endsWith('_Sep') ||
//                     input.name.endsWith('_Oct') || input.name.endsWith('_Nov') || input.name.endsWith('_Dec') ||
//                     input.name.endsWith('_Jan') || input.name.endsWith('_Feb') || input.name.endsWith('_Mar')) {
//                     totalExpenses += parseInt(input.value) || 0;
//                 }
//             });
//              console.log("ho")
//              console.log(totalExpenses)
//              console.log(row.querySelector('td input[name$="expenses"]'))
             
//              row.querySelector('td input[name$="expenses"]').value = totalExpenses;

//         });
//     }
//     function calculateAndDisplayClosingBalance(tableId) {
//         const table = document.querySelector(`#${tableId}`);
//         const rows = table.querySelectorAll('tr:not(.header-row)');
    
//         rows.forEach(function (row) {
//             // Skip the calculation for the "Total Amount" row
//             // if (row.querySelector('th').textContent.trim() === 'Total Amount') {
//             //     return;
//             // }
    
//             const grantAmount = parseInt(row.querySelector('input[name$="_Grant_Amount"]').value) || 0;
//             const totalExpenses = parseInt(row.querySelector('td input[name$="expenses"]').value) || 0;
    
//             // Use the correct name attribute for closing balance
//             const closingBalanceElement = row.querySelector('td[name$="_closing"]');
            
//             if (closingBalanceElement) {
//                 const closingBalance = grantAmount - totalExpenses;
//                 closingBalanceElement.textContent = closingBalance;
//                 if (closingBalance < 0) {
//                     closingBalanceElement.classList.add('negative-balance');
//                 } else {
//                     closingBalanceElement.classList.remove('negative-balance');
//                 }
//             }
//         });
//     }
//     function calculateAndDisplayTotalAmount(tableId) {
//         const table = document.querySelector(`#${tableId}`);
//         const headerRow = table.querySelector('.header-row');
//         const totalAmountRow = table.querySelector('tr[name="total_amount"]');
//         const totalAmountCells = totalAmountRow.querySelectorAll('td'); // Use 'td' instead of 'input'
//         // console.log(table)
//         // console.log(headerRow)
//         // console.log(totalAmountRow)
//         // console.log(totalAmountCells)
    
//         totalAmountCells.forEach(function (totalAmountCell, index) {
//             if(index==2){

//                 const grantAmountOne = parseInt(table.querySelector('input[name$="one_Grant_Amount"]').value) || 0;
//                 // const grantAmountTwo = parseInt(table.querySelector('input[name$="two_Grant_Amount"]').value) || 0;
//                 // const grantAmountThree = parseInt(table.querySelector('input[name$="three_Grant_Amount"]').textContent) || 0;
//                 // const grantAmountFour = parseInt(table.querySelector('input[name$="four_Grant_Amount"]').textContent) || 0;
//                 // const grantAmountFive = parseInt(table.querySelector('input[name$="five_Grant_Amount"]').textContent) || 0;
//                 // const grantAmountSix = parseInt(table.querySelector('input[name$="six_Grant_Amount"]').textContent) || 0;
//                 // const grantAmountSeven = parseInt(table.querySelector('input[name$="seven_Grant_Amount"]').textContent) || 0;
//                 const grantAmountTwo = parseInt(table.querySelector('input[name$="two_Grant_Amount"]').value) || 0;
//                 const grantAmountThree = parseInt(table.querySelector('input[name$="three_Grant_Amount"]').value) || 0;
//                 const grantAmountFour = parseInt(table.querySelector('input[name$="four_Grant_Amount"]').value) || 0;
//                 const grantAmountFive = parseInt(table.querySelector('input[name$="five_Grant_Amount"]').value) || 0;
//                 const grantAmountSix = parseInt(table.querySelector('input[name$="six_Grant_Amount"]').value) || 0;
//                 const grantAmountSeven = parseInt(table.querySelector('input[name$="seven_Grant_Amount"]').value) || 0;


//                 const totalGrantAmount = grantAmountOne + grantAmountTwo + grantAmountThree + grantAmountFour +grantAmountFive + grantAmountSix + grantAmountSeven;

//     // Update the content of the Total Grant Amount cell
//     const correspondingTotalAmountCell = totalAmountRow.querySelector(`td:nth-child(${index + 1})`);
//     // console.log("hi")
//     // console.log(totalGrantAmount)
//     // console.log("hi")
//     correspondingTotalAmountCell.innerHTML = `
//                     <input type='number' name='total_Grant_Amount' value='${totalGrantAmount}' >
//                 `;
//             }
           
//             if (index > 2) {  // Exclude S.No and Budget Head columns
//                 let totalAmount = 0;
//                 let month;
//                 // Iterate through rows (excluding header and total amount rows)
//                 const rows = table.querySelectorAll('tr:not(.header-row):not([name="total_amount"])');
//                 // console.log(rows)
//                 rows.forEach(function (row) {
//                   //  const inputField = row.querySelector(`input[name$="_${headerRow.cells[index].textContent.trim()}"]`);
//                    month = convertToInputFieldName(headerRow.cells[index].textContent.trim());
//                     const inputField = row.querySelector(`input[name*="_${convertToInputFieldName(headerRow.cells[index].textContent.trim())}"]`);
//                     // console.log(inputField)
//                     // console.log(headerRow.cells[index].textContent.trim())
//                     // console.log(convertToInputFieldName(headerRow.cells[index].textContent.trim()))
//                     if (inputField) {
//                         totalAmount += parseInt(inputField.value) || 0;
//                     }
//                     // console.log(totalAmount)
//                 });
//                 // console.log("end")
//                 // console.log(totalAmountCell)
//                 const correspondingTotalAmountCell = totalAmountRow.querySelector(`td:nth-child(${index + 1})`);
//                 // console.log(correspondingTotalAmountCell)
//                 //totalAmountCell.textContent = totalAmount;
//                 if (correspondingTotalAmountCell) {
//                 // Update the content of the total amount cell
//                 correspondingTotalAmountCell.innerHTML = `
//                     <input type='number' name='total_${month}' value='${totalAmount}'>
//                 `;
//             }
//             }
//         });
//     }
   
   
//     function convertToInputFieldName(monthText) {
//         // Add logic here to convert "Nov-2023" to "Nov"
//         // You may need to adjust this based on your specific requirements
//         const monthAbbreviation = monthText.split('-')[0];
//         return monthAbbreviation;
//     }
    
//     // JavaScript code
//     function saveTableDataToDjango(data, project_id) {
//         console.log(JSON.stringify(data));
//         fetch(`/save_table_data/${project_id}/`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': getCookie('csrftoken')
//             },
//             body: JSON.stringify(data)
//         })
//         .then(response => response.json())
//         .then(result => {
//             console.log(result);
//             // Handle success or error as needed
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     }

//     function getCookie(name) {
//         let cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             const cookies = document.cookie.split(';');
//             for (let i = 0; i < cookies.length; i++) {
//                 const cookie = cookies[i].trim();
//                 // Check if the cookie name matches the desired name
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }    


