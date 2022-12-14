const $$= document.querySelectorAll.bind(document)
const $ = document.querySelector.bind(document)
const modal = $('.modal');
const search = $('.search');
const fechar = $('.fechar');
search.onclick = function ()
{
    modal.style.display = 'block';

}
fechar.onclick = function ()
{
    modal.style.display = 'none';
}

// -----------------hover-img------------------------

const cards=$$('.card')
const imgs=$$('.card-img img');
const cardlinks=$$('.card-link')
imgs.forEach((img, index) => {
    if(img.src=='https://bom.so/ldBNOr')
    {
        img.onmouseover= function()
        {
            img.src='https://bom.so/rRvOnI'
        }
        img.onmouseout =function()
        {
            img.src="https://bom.so/ldBNOr"
        }
    }

    if(img.src=='https://bom.so/Lu32NY')
    {
        img.onmouseover= function()
        {
            img.src='https://bom.so/dViJ4r'
        }
        img.onmouseout =function()
        {
            img.src="https://bom.so/Lu32NY"
        }
    }

    if(img.src=='https://bom.so/8hpOZJ')
    {
        img.onmouseover= function()
        {
            img.src='https://bom.so/FAyJNx'
        }
        img.onmouseout =function()
        {
            img.src="https://bom.so/8hpOZJ"
        }
    }

    if(img.src=='https://bom.so/5EbrDd')
    {
        img.onmouseover= function()
        {
            img.src='https://bom.so/DqRKNb'
        }
        img.onmouseout =function()
        {
            img.src="https://bom.so/5EbrDd"
        }
    }

    
});


