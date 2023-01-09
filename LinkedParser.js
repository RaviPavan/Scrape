//Interaction code start
country('us')
try{
  let url = "https://www.linkedin.com/in/williamhgates" //new URL(input.url)
  navigate(url, {timeout: 8e4, solve_captcha: true});  
  if(!el_exists('meta[name="locale"][content="en_US"]')){
    throw new Error('Wrong localization '+parse().locale)
  }
}catch(e){
  if(e.message.includes('status 404')){ 
    return collect({message: `Account is private or link is invalid. Couldn't collect data`, url: input.url})
  }
  else throw(e.message)
//   else throw('Error. It is not possible to get this profile at the moment')
}

let data = parse();
collect({url: new URL(input.url), ...data, avatar: data?.avatar ? new URL(data?.avatar) : null});
//Interaction code end

//parser start
let trim = str=>(str||'').replace(/\s+/g, ' ').trim()
const URL_ = (u)=>{
    return !!u && new URL(u)||undefined
}
const Image_=(u)=>{
    return !!u && new Image(u)||undefined
}
let parse_duration = el=>{
    let contents = el.contents().toArray().map(v=>$(v).text().trim()).filter(v=>v&&v.length>1);
    return {
        duration: contents.join(' '),
        start_date: contents[0],
        end_date: contents[1] == '- Present' ? 'Present' : contents[1],
        duration_short: contents.slice(2).join(' '),
    }
}
let get_url = str=>{
    try {
        return decodeURIComponent(new URL(str).searchParams.get('url'));
    } catch(e){}
    return null;
}
let get_experience = ()=>{
    let data = $('.experience__list li.experience-item').toArray().map(item=>{
        if ($(item).find('.experience-group-header__company').text())
        {
            return {
                
                company: trim($(item).find('.experience-group-header__company').text()),
                duration: trim($(item).find('.experience-group-header__duration').text()),
                url: URL_($(item).find('a').attr('href')),
                positions: $(item).find('.experience-group__positions .result-card, .experience-group__positions .experience-group-position').toArray().map(_item=>({
                    title: $(_item).find('.result-card__title, .profile-section-card__title').text_sane(),
                    subtitle: trim($(_item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
                    meta: trim($(_item).find('.result-card__meta p, .profile-section-card__meta p').toArray().map(info=>{
                        let duration_text = trim($(info).find('.date-range__duration').text());
                        return $(info).text().replace(duration_text, ' '+duration_text);
                    }).join(', ')),
                    description: trim($(_item).find('.show-more-less-text__text--more').text()) || trim($(_item).find('.show-more-less-text__text--less').text()),
                    ...parse_duration($(_item).find('.result-card__meta .date-range, .profile-section-card__meta .date-range')),
                })),
            };
        }
        return {
            title: $(item).find('.result-card__title, .profile-section-card__title').text_sane(),
            subtitle: trim($(item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
            subtitleURL: URL_($(item).find('.result-card__subtitle > a, .profile-section-card__subtitle > a').attr('href')),
            location: trim($(item).find('.experience-item__location').text()),
            description: $(item).find('.show-more-less-text__text--more').text_sane() || $(item).find('.experience-item__meta-item .show-more-less-text__text--less, .experience-item__description .show-more-less-text').text_sane(),
            ...parse_duration($(item).find('.result-card__meta .date-range, .profile-section-card__meta .date-range')),
        }
    });
    return data;
};


function get_activities(){
    return $('section.activities').find('.activities-section__item--posts')
        .toArray().map(item=>{
            let link = $(item).find('a.activity-card__link, .base-card__full-link').attr('href');
            try {
                link = URL_(decodeURIComponent(new URL(link).searchParams.get('session_redirect')));
            } catch(e){}
            return {
                title: trim($(item).find('h3.activity-card__title, .base-main-card__title').text()),
                attribution: trim($(item).find('.activity-card__attribution, .base-main-card__subtitle').text()),
                img: Image_($(item).find('img.activity-card__image').attr('src') || $(item).find('img.main-activity-card__img').attr('data-delayed-url')),
                link,
            }
        })
}

function get_posts(){
    return $('section.activities').find('.activities-section__item--articles')
        .toArray().map(item=>{
            let link = URL_($(item).find('a.base-card--link').attr('href'));
            let time =  $(item).find(".base-main-card__metadata-item");
            return {
                title: trim($(item).find('h3.activity-card__title, .base-main-card__title').text()),
                attribution: trim($(item).find('.activity-card__attribution, .base-main-card__subtitle').text()),
                img: Image_($(item).find('.base-main-card__media img').attr('src') || $(item).find('.base-main-card__media img').attr('data-delayed-url')),
                link,
                created_at: time.text().trim() ? new Date(time.text().trim()).toISOString() : ""
            }
        })
}

function get_patents_date(patent_date)
{
    let time_arr = new Date(patent_date).toLocaleDateString()?.split("/")
    if(time_arr.length != 3)
        return {}
    return {
        "day": time_arr[1],
        "year": time_arr[2],
        "month": time_arr[0]
    }
}

let name = $('h1.top-card-layout__title').text_sane();
let position = $('h2.top-card-layout__headline').text_sane();
let about = $(".summary p").text_sane();
if (!name && !position && !about)
    return {"error_message": 'Profile does not exist'};
const followers = $('h3.top-card-layout__first-subline .top-card__subline-item:contains("follower")')?.text()?.replace(/\D+/g, '').trim() || null,
    connections = $('h3.top-card-layout__first-subline .top-card__subline-item:contains("connection")')?.text()?.replace(/\D+/g, '').trim() || null;
return {
    locale:$('meta[name="locale"][content]').attr('content'),
    name,
    position,
    current_company: {
        name: $('[data-section="currentPositionsDetails"] .top-card-link').text_sane(),
        link: URL_($('[data-section="currentPositionsDetails"] .top-card-link').attr('href')),
    },
    avatar: $('.top-card__profile-image-container img').attr('src') || $('.top-card__profile-image-container img').attr('data-delayed-url'),
    about,
    city: trim($('h3.top-card-layout__first-subline div').eq(0).text()),
    following: null,
    followers: followers ? +followers : null,
    connections: connections ? +connections : null,
    educations_details: trim($('.top-card__links-container [data-section="educationsDetails"]').text()),
    posts: get_posts(),
    experience: JSON.stringify(get_experience()),
    education: $('[data-section="educationsDetails"] .education__list li').toArray().map(item=>({
        title: trim($(item).find('.result-card__title, .profile-section-card__title').text()),
        degree: trim($(item).find('.result-card__subtitle > span:nth-child(1), .profile-section-card__subtitle > span:nth-child(1)').text()),
        field: trim($(item).find('.result-card__subtitle > span:nth-child(2), .profile-section-card__subtitle > span:nth-child(2)').text()),
        meta: trim($(item).find('.result-card__meta, .profile-section-card__meta').text()),
        url: URL_($(item).find('li > a').attr('href')),
        start_year: trim($(item).find('.education__item--duration time:nth-child(1)').text()),
        end_year: trim($(item).find('.education__item--duration time+ time').text()),
    })),
    certifications: $('[data-section="certifications"] .certifications__list li').toArray().map(item=>({
        title: trim($(item).find('.result-card__title, .profile-section-card__title').text()),
        subtitle: trim($(item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
        meta: trim($(item).find('.result-card__meta, .profile-section-card__meta').text()),
    })),
    courses: $('[data-section="courses"] .courses__list li').toArray().map(item=>({
        title: trim($(item).find('.result-card__title, .profile-section-card__title').text()),
        subtitle: trim($(item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
        meta: trim($(item).find('.result-card__meta, .profile-section-card__meta').text()),
    })),
    languages: $('[data-section="languages"] .languages__list li').toArray().map(item=>({
        title: trim($(item).find('.result-card__title, .profile-section-card__title').text()),
        subtitle: trim($(item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
        meta: trim($(item).find('.result-card__meta, .profile-section-card__meta').text()),
    })),
    groups: $('[data-section="groups"]  li').toArray().map(item=>({
        img: Image_($(item).find('img').attr('src')),
        title: trim($(item).find('.result-card__title, .profile-section-card__title').text()),
        subtitle: trim($(item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
        meta: trim($(item).find('.result-card__meta, .profile-section-card__meta').text()),
    })),
    people_also_viewed: $('section.browsemap.right-rail-section > div > ul > li, .right-rail .aside-section-container.browsemap >div > div > ul > li').toArray().map(item=>({
        //img: $(item).find('img').attr('src'),
        profile_link: URL_($(item).find('a').attr('href'))
    })),
    activities: get_activities(),
    recommendations: $('[data-section="recommendations"] .recommendations__list-item').toArray().map(v=>trim($(v).text())),
    recommendations_count: (+trim($('.recommendations__count').text()).split(' ')[0])||null,
    volunteer_experience: $('[data-section="volunteering"] .volunteering__list li').toArray().map(item=>({
        title: trim($(item).find('.result-card__title, .profile-section-card__title').text()),
        subtitle: trim($(item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
        cause: trim($(item).find('.volunteering__item--cause').text()),
        url: URL_($(item).find('li > a').attr('href')),
        ...parse_duration($(item).find('.result-card__meta .date-range, .profile-section-card__meta .date-range')),
        info: trim($(item).find('.result-card__meta .show-more-less-text, .profile-section-card__meta .show-more-less-text').text()),
    })),
    projects: $('.projects__list > li.result-card, .projects__list > .profile-section-card').toArray().map(item=>({
        img: Image_($(item).find('img').attr('src')),
        title: trim($(item).find('.result-card__title, .profile-section-card__title').text()),
        subtitle: trim($(item).find('.result-card__subtitle, .profile-section-card__subtitle').text()),
        meta: trim($(item).find('.result-card__meta .show-more-less-text, .profile-section-card__meta .show-more-less-text').text()),
        ...parse_duration($(item).find('.result-card__subtitle .date-range, .profile-section-card__subtitle .date-range')),
        url: URL_(get_url($(item).find('.result-card__title-link, .profile-section-card__title-link').attr('href'))),
    })),
    patents: $('[data-section="patents"] .patents__list > li').toArray().map(x=>(
        {
            "url": $(x).find('a.personal-project__button').attr("href")?.match(/(?<=url=).*?(?=&)/)?.[0] ? URL_(decodeURIComponent($(x).find('a.personal-project__button').attr("href")?.match(/(?<=url=).*?(?=&)/)?.[0])) : null,
            "title": trim($(x).find(".profile-section-card__title").text()),
            "issuer": trim($(x).find(".profile-section-card__subtitle :nth-child(2)").text()),
            "issued_on": get_patents_date(trim($(x).find(".profile-section-card__subtitle time").text())) ,
            "description": null,
            "patent_number": trim($(x).find(".profile-section-card__subtitle :nth-child(3)").text()),
            "application_number": trim($(x).find(".profile-section-card__subtitle :nth-child(3)").text())
        })),
    publications: $('[data-section="publications"] .publications__list > li').toArray().map(x=>(
        {
            "url": $(x).find('a.personal-project__button').attr("href")?.match(/(?<=url=).*?(?=&)/)?.[0] ? URL_(decodeURIComponent($(x).find('a.personal-project__button').attr("href")?.match(/(?<=url=).*?(?=&)/)?.[0])) : null,
            "name": trim($(x).find(".profile-section-card__title").text()),
            "publisher": trim($(x).find(".profile-section-card__subtitle > :nth-child(1)").text()),
            "description": trim($(x).find(".show-more-less-text").text()),
            "published_on": get_patents_date(trim($(x).find(".profile-section-card__subtitle time").text()))
        })),
    awards:  $('[data-section="awards"] .awards__list > li').toArray().map(x=>(
        {
            "title": trim($(x).find(".profile-section-card__title").text()),
            "issuer": trim($(x).find(".profile-section-card__subtitle").text()),
            "issuedOn": trim($(x).find(".profile-section-card__meta time").text()) ? new Date(trim($(x).find(".profile-section-card__meta time").text()) ).toISOString() : null,
            "description": null
        })),
    timestamp: new Date(),
};

