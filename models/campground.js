const mongoose = require('mongoose');
const Schema = mongoose.Schema; //making a shorthand variable

//separate image into it's own schema so we can add virtual schema to it
const ImageSchema = new Schema({
    url: String, 
    filename: String
})
ImageSchema.virtual('thumbnail').get(function(){
    return this.url.replace('/upload', '/upload/w_300');
})

const opts = {toJSON: {virtuals: true}};

const campGroundSchema = new Schema({
    title: String,
    image: [ImageSchema],
    geometry: {
        type: {
            type: String,
            enum: ['Point'],
            required: true
        },
        coordinates: {
            type: [Number],
            required: true
        }
    },
    price: Number,
    description: String,
    location: String,
    author: {
        type: Schema.Types.ObjectId,
        ref: 'User'
    },
    reviews: [
        {
            type: Schema.Types.ObjectId,
            ref: 'Review' //from Review Model
        }
    ]
}, opts)

campGroundSchema.virtual('properties.popUpMarkup').get(function(){
    return `
    <strong><a href="/campgrounds/${this._id}">${this.title}</a><strong>
    <p>${this.description.substring(0, 45)}...</p>`;
})

module.exports = mongoose.model('CampGround', campGroundSchema);