// --------------------product size guide---------------------
    
const modalproduct = $('.modal-product');
const sizeguide = $('.size-guide p')
sizeguide.onclick = function ()
{
    modalproduct.style.display = 'block';
}
const closeproduct = $('.close-product');
closeproduct.onclick = function ()
{
    modalproduct.style.display = 'none';
}