var data_product = [
    {
      "id": 1,
      "name": "T-Shirt#1",
      "price": "200.000",
      "href": "https://bom.so/ldBNOr",
      "itemNo":"CK1-70900295_BLACK"
    },
    {
      "id": 2,
      "name": "T-Shirt#2",
      "price": "230.000",
      "href": "https://bom.so/Lu32NY",
      "itemNo":"CK1-70900295_BLACK"
    },
    {
      "id": 3,
      "name": "T-Shirt#3",
      "price": "280.000",
      "href": "https://bom.so/8hpOZJ",
      "itemNo":"CK1-70900295_BLACK"
    },
    {
      "id": 4,
      "name": "T-Shirt#4",
      "price": "240.000",
      "href": "https://bom.so/5EbrDd",
      "itemNo":"CK1-70900295_BLACK"
    },
  {
      "id": 5,
      "name": "T-Shirt#5",
      "price": "360.000",
      "href": "https://bom.so/5EbrDd",
      "itemNo":"CK1-70900295_BLACK"
  }
]
var toAdd = document.createDocumentFragment();
for (var i = 0; i < data_product.length; i++){
  // <div class="col-lg-3">
  var newDiv = document.createElement('div');
  newDiv.className = 'col-lg-3 product-item';
  newDiv.id=`${data_product[i].id}`
  // <a class="card-link" href="#">
  const newa = document.createElement('a')
  newa.className = 'card-link';
  newa.href = './product-item.html';
  //<div class="card" style="width: 15rem;">
  const newa_div = document.createElement('div');
  newa_div.className = "card";
  newa_div.style = 'width: 15rem;';
    // <div class="card-img">
  const newa_div_div1 = document.createElement('div');
  newa_div_div1.className = 'card-img';
  //<img src="https://bom.so/ldBNOr" class="card-img-top" alt="...">
  const newa_div_div1_img = document.createElement('img');
  newa_div_div1_img.className = 'card-img-top';
  newa_div_div1_img.src = data_product[i].href;
  newa_div_div1_img.alt = '#';
  // <div class="card-body"></div>
  const newa_div_div2 = document.createElement('div');
  newa_div_div2.className = 'card-body';
  const newa_div_div2_p1 = document.createElement('p');
  //name t-shirt
  newa_div_div2_p1.className = 'card-text';
  newa_div_div2_p1.innerText = data_product[i].name;

  const newa_div_div2_p2 = document.createElement('p');
  //price
  newa_div_div2_p2.className =  'price';
  newa_div_div2_p2.innerText = data_product[i].price;

    
  newa_div_div1.appendChild(newa_div_div1_img);
  newa_div.appendChild(newa_div_div1);
  newa_div_div2.appendChild(newa_div_div2_p1)
  newa_div_div2.appendChild(newa_div_div2_p2)
  newa_div.appendChild(newa_div_div2);
  newa.appendChild(newa_div);
  newDiv.appendChild(newa);
  toAdd.appendChild(newDiv);
}
$('.row.products').append(toAdd);
document.appendChild(toAdd);

// // --product-item
// const product_item = document.getElementById('1');
// console.log(product_item);

// const handleClick = function (e) {
//   e.preventDefault();
//   console.log(e);
// }
// product_item.addEventListener('click', handleClick());

// const a = data_product.find((product) => {
//   return product.id == 2
 
// });

//--product-item
// const html = data_product.find(index =>
//   `<h3>${T-SHIRT}</h3>
//   <p>Item No.${data_product}</p>
//   </div>
//   <p class="price">
//     $50.00 USD
//   </p>
//   <div class="size">
//     <span>S</span>
//     <span>M</span>
//     <span>XL</span>
//     <span>XXL</span>
//   </div>
//   <div class="size-guide row">
//     <i class="fa-solid fa-ruler"></i>
//     <p>Size guide</p>`)
