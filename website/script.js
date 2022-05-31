$(document).ready(function(){
    $.getJSON('keywords.json', function(data){
        // Число кластеров
        const number = Object.keys(data.keywords).length;
        // Находим div.articles в html
        let articleDiv = document.querySelector(".articles"); 
        let topicsDiv = document.querySelector(".topics");
        // Создаем div.cluster согласно числу кластеров
        for (let i = 0; i < number; i++) {
            let cluster = document.createElement('div');
            cluster.classList.add('cluster');

            // Добавляем в каждый кластер ключевые слова         
            let hEl = document.createElement('h2');
            hEl.id = 'cluster' + (i + 1);
            let keywordList = ((data.keywords[i])[0]).toUpperCase() 
                + data.keywords[i].slice(1);
            hEl.textContent = keywordList;
            cluster.appendChild(hEl);
            
            let linkEl = document.createElement('a');
            linkEl.textContent = data.keywords[i];
            linkEl.classList.add('topicLink');
            linkEl.href = '#' + hEl.id;
            let topicDiv = document.createElement('li');
            topicDiv.append(linkEl);
            topicsDiv.appendChild(topicDiv);

            // Добавляем список
            let list = document.createElement('ol');   
            $(document).ready(function(){        
                $.getJSON('base.json', function(data){
                    const len = Object.keys(data.authors).length;
                    let count = 0;
                    for (let j = 1; j < len; j++) {
                        if (data.cluster[j] == i) {               
                            let li = document.createElement('li');
                            if (!(data.year[j] == "NULL")) {
                                li.textContent = data.authors[j] + "."
                            }
                                
                            if (!(data.authors[j] == "NULL")) {
                                li.textContent += " (" + data.year[j] + ")."
                            }
                                
                            if (!(data.title[j] == "NULL")) {
                                li.textContent += " " + data.title[j] + '. '
                            }                             
                            li.textContent += "Supercomputing Frontiers and Innovations"
                            if (!(data.number[j] == "NULL")) {
                                li.textContent += ', ' + data.number[j] + '.'
                            }                              
                            else {
                                li.textContent += "."
                            } 
                            li.textContent += " doi: ";
                            let link = document.createElement('a');
                            link.textContent = data.doi[j];
                            link.href = 'https://doi.org/' + data.doi[j];
                            link.target = '_blank';
                            if (count >= 5) {
                                li.classList.add('hide');
                            }  
                            li.appendChild(link);
                            list.appendChild(li);     
                            count += 1;              
                        } 
                    }
                })
            });
            cluster.appendChild(list);
            let btn = document.createElement('button');
            btn.classList.add('clusterBtn');
            btn.textContent = 'More';
            btn.addEventListener('click', ShowArticles);
            cluster.appendChild(btn);  
            articleDiv.appendChild(cluster);   
        }            
    });
});

function ShowArticles() {
    if (this.textContent === 'Less') {
        this.textContent = 'More';
    } else if (this.textContent === 'More') {
        this.textContent = 'Less';
    }

    this.parentElement.querySelectorAll('li:nth-child(n+11)')
        .forEach(el => el.classList.toggle('hide'));
}