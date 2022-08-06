const express = require('express');
const app = express();
const path = require('path');
const mongoose = require('mongoose');
const ejsMate = require('ejs-mate');
// const {campgroundSchema} = require('./schemas')
// const {reviewSchema} = require('./schemas')
// const catchAsync = require('./utils/catchAsync');
const ExpressError = require('./utils/ExpressError');
// const campGround = require('./models/campground');
// const Review = require('./models/review');
const methodOverride = require('method-override');
const campgroundRoutes = require('./routes/campgrounds') 
const reviewRoutes = require('./routes/reviews') 

mongoose.connect('mongodb://localhost:27017/yelp-camp')
    .then(()=> {
        console.log("MongoDB Connection Opened!");
    })
    .catch((error) =>{
        console.log("Oh no, database connection error!")
        console.log(error);
    })

app.engine('ejs', ejsMate);    
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));

app.use(express.urlencoded({extended: true}));
app.use(express.json());
app.use(methodOverride('_method'));

app.use('/campgrounds', campgroundRoutes)
app.use('/campgrounds/:id/reviews', reviewRoutes)


// const validateCampground = (req, res, next) => {
//     const { error } = campgroundSchema.validate(req.body);
//     if(error){
//         const msg = error.details.map(el => el.message).join(',');
//         throw new ExpressError(msg, 400)
//     }
//     else{
//         next()
//     }
// }

// const validateReview = (req, res, next) => {
//     const { error } = reviewSchema.validate(req.body);
//     if(error){
//         const msg = error.details.map(el => el.message).join(',');
//         throw new ExpressError(msg, 400)
//     }
//     else{
//         next()
//     }
// }


// app.get('/campgrounds', catchAsync(async (req, res) => {
//     const campgrounds = await campGround.find({});
//     res.render('campgrounds/index', {campgrounds});
// }))

// app.get('/campgrounds/new', (req, res) => {
//     res.render('campgrounds/new'); 
// })

// app.post('/campgrounds', validateCampground, catchAsync(async (req, res, next) => {
//     // if(!req.body.campground) throw new ExpressError('Invalid Campground Data', 400);
//     const newGround = new campGround(req.body.campground);
//     await newGround.save();
//     res.redirect(`/campgrounds/${newGround._id}`);
// }))

// app.get('/campgrounds/:id', catchAsync(async (req, res) => {
//     const {id} = req.params;
//     const foundcampground = await (await campGround.findById(id)).populate('reviews');
//     res.render('campgrounds/show', {foundcampground}); 
// }))

// app.get('/campgrounds/:id/edit', catchAsync(async (req, res) => {
//     const {id} = req.params;
//     const foundcampground = await campGround.findById(id);
//     res.render('campgrounds/edit', {foundcampground}); 
// }))

// app.put('/campgrounds/:id', validateCampground, catchAsync(async (req, res) => {
//     const {id} = req.params;
//     const updatedGround = await campGround.findByIdAndUpdate(id, {...req.body.campground});
//     res.redirect(`/campgrounds/${updatedGround._id}`);
// }))

// app.delete('/campgrounds/:id', catchAsync(async (req, res) => {
//     const {id} = req.params;
//     const deletedCampGround = await campGround.findByIdAndDelete(id);
//     if(deletedCampGround.reviews.length){
//         await Review.deleteMany({_id: {$in: deletedCampGround.reviews}})
//     }
//     res.redirect('/campgrounds');
// }))


// app.post('/campgrounds/:id/reviews', validateReview, catchAsync(async(req, res) => {
//     const {id} = req.params;
//     const foundcampground = await campGround.findById(id); //found campground we're going to associate with review
//     const newReview = new Review(req.body.review); //creating new review
//     foundcampground.reviews.push(newReview); //pushing reference to new review onto campground document
//     await newReview.save();
//     await foundcampground.save();
//     res.redirect(`/campgrounds/${foundcampground._id}`);
// }))

// app.delete('/campgrounds/:id/reviews/:review_id', catchAsync(async(req, res) => {
//     const {id, review_id} = req.params;
//     await campGround.findByIdAndUpdate(id, {$pull: {reviews: review_id}}); //found campground and remove review reference
//     await Review.findByIdAndDelete(review_id); //found review we're going to remove 
//     res.redirect(`/campgrounds/${id}`);
// }))


app.all("*", (req, res, next)=>{
    next(new ExpressError('Page Not Found', 404))
})

app.use((err, req, res, next)=>{
    const {statusCode = 500} = err;
    if(!err.message){
        err.message = "Something went wrong!"
    }
    res.status(statusCode).render('error', {err});
})


app.listen(3000, () => {
    console.log('Serving on port 3000!')
})