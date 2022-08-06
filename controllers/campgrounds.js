const campGround = require('../models/campground');
const { cloudinary } = require("../cloudinary");
const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding');
const mapBoxToken = process.env.MAPBOX_TOKEN;
const geocoder = mbxGeocoding({accessToken: mapBoxToken})


module.exports.index = async (req, res) => {
    const campgrounds = await campGround.find({});
    res.render('campgrounds/index', {campgrounds});
}

module.exports.renderNewForm = (req, res) => {
    res.render('campgrounds/new'); 
}

module.exports.createCampground = async (req, res, next) => {
    // if(!req.body.campground) throw new ExpressError('Invalid Campground Data', 400);
    const geoData = await geocoder.forwardGeocode({
        query: req.body.campground.location,
        limit: 1
    }).send()
    const newGround = new campGround(req.body.campground);
    newGround.geometry = geoData.body.features[0].geometry;
    for(let file of req.files){
        newGround.image.push({url: file.path, filename: file.filename})
    }
    newGround.author = req.user._id;
    await newGround.save();
    console.log(newGround);
    req.flash('success', 'Successfully made a new campground!');
    res.redirect(`/campgrounds/${newGround._id}`);
}

module.exports.showCampground = async (req, res) => {
    const {id} = req.params;
    const foundcampground = await campGround.findById(id).populate({
        path: 'reviews',
        populate: {
            path: 'author'
        }
    }).populate('author');
    if(!foundcampground){
        req.flash('error', 'Cannot find that campground!');
        return res.redirect('/campgrounds');
    }
    res.render('campgrounds/show', {foundcampground}); 
}

module.exports.renderEditForm = async (req, res) => {
    const {id} = req.params;
    const foundcampground = await campGround.findById(id);
    if(!foundcampground){
        req.flash('error', 'Cannot find that campground!');
        return res.redirect('/campgrounds');
    }
    res.render('campgrounds/edit', {foundcampground}); 
}

module.exports.updateCampground = async (req, res) => {
    const {id} = req.params;
    const updatedGround = await campGround.findByIdAndUpdate(id, {...req.body.campground});
    for(let file of req.files){
        updatedGround.image.push({url: file.path, filename: file.filename})
    }
    await updatedGround.save();
    if(req.body.deleteImages){
        for(let filename of req.body.deleteImages){
            await cloudinary.uploader.destroy(filename);
        }
        await updatedGround.updateOne({$pull: {image: {filename: {$in: req.body.deleteImages}}}});
    }
    req.flash('success', 'Successfully updated campground!');
    res.redirect(`/campgrounds/${updatedGround._id}`);
}

module.exports.deleteCampground = async (req, res) => {
    const {id} = req.params;
    const deletedCampGround = await campGround.findByIdAndDelete(id);
    if(deletedCampGround.reviews.length){
        await Review.deleteMany({_id: {$in: deletedCampGround.reviews}})
    }
    req.flash('success', 'Successfully deleted campground!');
    res.redirect('/campgrounds');
}