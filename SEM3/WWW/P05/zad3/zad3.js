function removeImg(src){
    let start = src.indexOf("<img");
    let end = src.indexOf("/>");
    let toRemove = src.slice(start, end+2);
    src = src.replace(toRemove, "");
    return src;
}

function transform() {
    return function (desc, render) {
        return removeImg(render(desc));
    };
}

$(document).ready(function() {
    $.getJSON('tvn24.json', {}, function (data) {
        let news = data.rss.channel.item.slice(0, 5);
        let content = Mustache.render(`
            {{#news}}
                <tr>
                    <td>{{title}}</td>
                    <td><a href='{{{link}}}'>{{link}}</a></td>
                    <td>
                        {{#transform}}
                            {{{description.__cdata}}}
                        {{/transform}}
                    </td>
                </tr>
            {{/news}}
        `, {news, transform});

        $("#container").append(content);
    }
)});