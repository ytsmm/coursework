$(document).ready(function(){
    $.getJSON('base.json', function(data){
        let number = []
        for (let i = 0; i < Object.keys(data.cluster).length; i++) {
            if (!(data.cluster[i] in number)) {
                number.push(data.cluster[i]);
            }
        }

        let articleDiv = document.querySelector("div.articles");
   
        for (let i = 0; i < number.length; i++) {
            let div = document.createElement('div');
            div.classList.add('cluster');
            let list = document.createElement('ol');    
            let btn = document.createElement('button');
            btn.classList.add('articlesBtn');
            btn.textContent = 'Show more';
            btn.addEventListener('click', ShowArticles);

            let count = 0;
            for (let j = 0; j < Object.keys(data.doi).length; j++) {               
                if (data.cluster[j] == i) {                  
                    let li = document.createElement('li');

                    let link = document.createElement('a');
                    link.href = 'https://doi.org/' + data.doi[j];
                    link.target = '_blank';
                    link.textContent = data.title[j];
                    if (count >= 10) {
                        li.classList.add('hide');
                    }

                    li.append(link);
                    list.append(li);     
                    count += 1;              
                }                          
            }
            div.appendChild(list);
            div.appendChild(btn);
            articleDiv.appendChild(div);
        }
    });
});

$(document).ready(function(){
    $.getJSON('keywords.json', function(data){
        let artEl = document.querySelectorAll('.cluster');
        for (let i = 0; i < Object.keys(data.keywords).length; i++) {
            console.log(artEl[i]);
            let hEl = document.createElement('h2');
            hEl.textContent = data.keywords[i];
            artEl[i].prepend(hEl);
        }
   
    });
});

function ShowArticles() {
    if (this.textContent === 'Show less') {
        this.textContent = 'Show more';
    } else if (this.textContent === 'Show more') {
        this.textContent = 'Show less';
    }

    this.parentElement.querySelectorAll('li:nth-child(n+11)')
        .forEach(el => el.classList.toggle('hide'));
}