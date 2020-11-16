$.get({dataType: "text", url:"./tvn24.xml"}).done(downloaded);

var parsed;

function downloaded(data){
    parsed = $.parseXML(data); //sparsowany xml
    console.log(parsed);
    var find = $(parsed).find("item");
    let i = 0;
    find.each(function () {
        if(i == 5){ //5 artykułów
            return 0;
        }
        i++;

        var find_title = $(this).find("title");
        var find_link = $(this).find("link");
        var find_desc = $(this).find("description");

        var title = $(find_title).text();
        var link = $(find_link).text();
        var desc = $(find_desc).text();

        $("#container").append("<tr><td class=\"title\">" + title + "</td>" +
                                "<td><a href=\"" + link + "\">" + link +  "</a></td>" +
                                "<td>" + removeImg(desc) + "</td></tr>");
    })
}

function removeImg(src){
    let start = src.indexOf("<img");
    let end = src.indexOf("/>");
    let toRemove = src.slice(start, end+2);
    src = src.replace(toRemove, "");
    return src;
}

function Search(){
    let sp = $("#searchphrase").val();

    $("#result  .result").remove();

    if(!parsed){
        return;
    }

    let items = $(parsed).xpath("/rss/channel/item");

    for (var i = 0; i<items.length; i++){
        let opis = $(items[i]).xpath("./description/text()")[1].data; //
        //console.log($(items[i]).xpath("./description/text()")); //zwraca częśc przed cdata cdata i po cdata

        if(opis.includes(sp)){            
            $("#result").append("<tr class=result><td class=\"title\">" + $(items[i]).xpath("./title/text()")[0].data + "</td>" +
                                    "<td><a href=\"" + $(items[i]).xpath("./link/text()")[0].data + "\">" + $(items[i]).xpath("./link/text()")[0].data +  "</a></td>" +
                                    "<td>" + removeImg(opis) + "</td></tr>");
        }
    }
}