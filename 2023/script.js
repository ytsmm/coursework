function getJson(url) {
    return fetch(url)
        .then(result => result.json())
        .catch(error => {
            console.log(error);
        })
}


function mounted(dataArt, dataClus, ar, cl, n) {
    this.getJson('./data.json')
        .then(data => {
            for (let el of data.articles) {
                dataArt.push(el);
                ar.push(JSON.stringify(el));
            }
            for (let el of data.clusters) {
                dataClus.push(el);
                cl.push(JSON.stringify(el));
            }
            n = data.clusterQuantity;
        });
 }

const articles = [];
const clusters = []
const ar = [];
const cl = [];
let number = 3;
mounted(articles, clusters, ar, cl, number);
setTimeout(() => {console.log(number);}, 1000)

let dataClass = [];
setTimeout(() => {
    for (let i of articles) {
        dataClass.push(i.class);     
    }

    const div = document.querySelector('div.articles');
    for (let i = 0; i < number; i++) {
        let articleClass = document.createElement('div');   
        let articleHeader = document.createElement('h3');  
        articleHeader.textContent = `Class ${i + 1}`;
        articleClass.append(articleHeader);
        let classKeywords = document.createElement('p');
        classKeywords.textContent = `Keywords: ${clusters[i].keywords}`;
        articleClass.append(classKeywords);
        let articleDiv = document.createElement('div');
        let k = 0;  
        for (let j = 0; j < dataClass.length; j++) {               
            if (dataClass[j] == i) {
                k++;
                console.log(k);
                if (k > 5) {
                    console.log(k);
                    break;
                }
                let name = document.createElement('h4');
                name.textContent = articles[j].title;
                articleDiv.append(name);

                let authors = document.createElement('p');
                authors.textContent = articles[j].authors;
                articleDiv.append(authors);

                articleDiv.append('DOI: ')
                let link = document.createElement('a');
                link.textContent = articles[j].doi;
                link.href = articles[j].doi;
                articleDiv.append(link);

                // let articleKeys = document.createElement('p');
                // articleKeys.textContent = `Keywords: ${linkKeys[j]}`;
                // articleDiv.append(articleKeys);
            }
            articleClass.append(articleDiv);
        }
        articleClass.append(document.createElement('br'));
        div.appendChild(articleClass);
    }
    
  }, 1000);
