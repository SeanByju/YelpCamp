const mongoose = require('mongoose');
const campGround = require('../models/campground');
const cities = require('./cities');
const {places, descriptors} = require('./seedHelpers');

mongoose.connect('mongodb://localhost:27017/yelp-camp')
    .then(()=> {
        console.log("MongoDB Connection opened!");
    })
    .catch((error) =>{
        console.log("Oh no, database connection error!")
        console.log(error);
    })

const sample = (array) => array[Math.floor(Math.random()* array.length)];


const seedDB = async () => {
    await campGround.deleteMany({});
    for(let i = 0; i < 200; i++){
        const random1000 = Math.floor(Math.random() * 1000);
        const price = Math.floor(Math.random() * 20) + 10;
        const camp = new campGround({
            //Your user id
            author: '62e86c415181a417ca68eb43',
            location: `${cities[random1000].city}, ${cities[random1000].state} `,
            title: `${sample(descriptors)} ${sample(places)}` ,
            description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quibusdam repudiandae recusandae, perspiciatis odit aliquid blanditiis pariatur natus vitae at labore enim tenetur magnam, tempora cumque alias aspernatur inventore, sint similique.",
            price,
            geometry: { 
                "type" : "Point", 
                "coordinates" : [ cities[random1000].longitude, cities[random1000].latitude ] 
            },
            image: [
                {
                    url: 'https://res.cloudinary.com/dcel4ewmg/image/upload/v1659571142/YelpCamp/i43h2gnxxy3cph8v0f4d.png',
                    filename: 'YelpCamp/i43h2gnxxy3cph8v0f4d',
                }
            ]
        })
        await camp.save();
   }
}

seedDB().then(()=>{
    mongoose.connection.close();
})