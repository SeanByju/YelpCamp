const campGround = require('../models/campground');
const Review = require('../models/review');

module.exports.createReview = async(req, res) => {
    const {id} = req.params;
    const foundcampground = await campGround.findById(id); //found campground we're going to associate with review
    const newReview = new Review(req.body.review); //creating new review
    newReview.author = req.user._id;
    foundcampground.reviews.push(newReview); //pushing reference to new review onto campground document
    await newReview.save();
    await foundcampground.save();
    req.flash('success', 'Successfully added your review!');
    res.redirect(`/campgrounds/${foundcampground._id}`);
}

module.exports.deleteReview = async(req, res) => {
    const {id, review_id} = req.params;
    await campGround.findByIdAndUpdate(id, {$pull: {reviews: review_id}}); //found campground and remove review reference
    await Review.findByIdAndDelete(review_id); //found review we're going to remove 
    req.flash('success', 'Successfully deleted your review!');
    res.redirect(`/campgrounds/${id}`);
}