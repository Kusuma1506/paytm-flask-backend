const API = "http://127.0.0.1:5000"


// CREATE USER
async function createUser(){

const name = document.getElementById("name").value
const balance = document.getElementById("balance").value

const res = await fetch(API + "/create-user",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
name:name,
balance:Number(balance)
})
})

const data = await res.json()

console.log(data)

document.getElementById("createMsg").innerText = data.message

document.getElementById("name").value=""
document.getElementById("balance").value=""

}



// CHECK BALANCE
async function checkBalance(){

const name=document.getElementById("balanceName").value

const res = await fetch(API + "/balance/" + name)

const data = await res.json()

console.log(data)

if(data.balance !== undefined){

document.getElementById("balanceResult").innerText =
"Balance: ₹ " + data.balance

}
else{

document.getElementById("balanceResult").innerText =
data.error

}

}



// SEND MONEY
async function sendMoney(){

const sender=document.getElementById("sender").value
const receiver=document.getElementById("receiver").value
const amount=document.getElementById("amount").value

const res = await fetch(API + "/send-money",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
sender:sender,
receiver:receiver,
amount:Number(amount)
})
})

const data = await res.json()

console.log(data)

document.getElementById("sendMsg").innerText=data.message

}



// LOAD TRANSACTIONS
async function loadTransactions(){

const res = await fetch(API + "/transactions")

const data = await res.json()

console.log(data)

const table=document.getElementById("txTable")

table.innerHTML=""

data.forEach(tx => {

const row = document.createElement("tr")
row.innerHTML = `
<td>${tx.sender}</td>
<td>${tx.receiver}</td>
<td>${tx.amount}</td>
`;

table.appendChild(row)

})

}