const {campgroundSchema, reviewSchema} = require('./schemas')
const ExpressError = require('./utils/ExpressError');
const campGround = require('./models/campground');
const Review = require('./models/review');

module.exports.isLoggedIn = (req, res, next) => {
    if(!req.isAuthenticated()){
        //store the url they are requesting
        req.session.returnTo = req.originalUrl //store orignal url in session object
        req.flash('error', 'you must be signed in');
        return res.redirect('/login');
    }
    next();
}

module.exports.validateCampground = (req, res, next) => {
    const { error } = campgroundSchema.validate(req.body);
    if(error){
        const msg = error.details.map(el => el.message).join(',');
        throw new ExpressError(msg, 400)
    }
    else{
        next()
    }
}

module.exports.isAuthor = async (req, res, next) => {
    const foundcampground = await campGround.findById(req.params.id);
    if(!foundcampground.author.equals(req.user._id)){
        req.flash('error', 'You do not have permission to do that!');
        return res.redirect(`/campgrounds/${req.params.id}`);
    }
    next();
}

module.exports.validateReview = (req, res, next) => {
    const { error } = reviewSchema.validate(req.body);
    if(error){
        const msg = error.details.map(el => el.message).join(',');
        throw new ExpressError(msg, 400)
    }
    else{
        next()
    }
}

module.exports.isReviewAuthor = async (req, res, next) => {
    const {id, review_id} = req.params;
    const foundReview = await Review.findById(review_id); //found review we're going to remove 
    if(!foundReview.author.equals(req.user._id)){
        req.flash('error', 'You do not have permission to do that!');
        return res.redirect(`/campgrounds/${id}`);
    }
    next();
}
