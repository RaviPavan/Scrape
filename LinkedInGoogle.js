let userid = input.url.split('/in/')[1].split('/')[0].split('?')[0];
let url = 'https://www.google.com/search?q=site:linkedin.com/in/' + userid
navigate(url)
let data = parse();
console.log(data);
if (userid == data.user_id)
	collect(data);

    //Parser

    return {
        "input_userid": input.url.split('/in/')[1].split('/')[0].split('?')[0],
        "link": $(".MjjYud").eq(0).find("a").attr("href"),
        "user_id": $(".MjjYud").eq(0).find("a").attr("href").split('/in/')[1],
        "location": $(".MjjYud").find(".MUxGbd.wuQ4Ob.WZ8Tjf").find("span").eq(0).text_sane(),
        "title": $(".MjjYud").find(".MUxGbd.wuQ4Ob.WZ8Tjf").find("span").eq(2).text_sane(),
        "company": $(".MjjYud").find(".MUxGbd.wuQ4Ob.WZ8Tjf").find("span").eq(4).text_sane(),   
        "name": $(".MjjYud").eq(0).find("h3").text_sane().split('-')[0].trim(),
      }