function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function show_notification(list)
{
    text = list[0];
    pos_class = list[1];
    company_name = list[2];
    company_url = list[3];

    live_time = getRandomInt(10000, 13000)
    let div = document.createElement('div');
    div.className = pos_class;
    div.innerHTML = text + '<div> от <a style="color:#1BB313; font-size: 18px;" href="'+company_url+'">'+company_name+'</a></div>';
    document.body.append(div);
    setTimeout(() => div.remove(), live_time);
}

function get_random_list(list){
    var item = list[Math.floor(Math.random()*list.length)];
    splited = item.split(' ');
    position = splited[0];
    company_name = splited[1];
    company_url = splited[2];

    text = '';
    for (var i = 3; i < splited.length; i++){
        text += splited[i] + ' ';
    }
    return [text, position, company_name, company_url]
}

function notification(args){
    setTimeout(() => show_notification(get_random_list(args)), getRandomInt(2000, 3000));
    setInterval(() => show_notification(get_random_list(args)), getRandomInt(13000, 20000));
}
