const express = require('express');
const router = express.Router(); 
const catchAsync = require('../utils/catchAsync');
const campGround = require('../models/campground');
const campgrounds = require('../controllers/campgrounds'); //will be an object with filled with functions we can import
const {isLoggedIn, validateCampground, isAuthor} = require('../middleware');
const multer  = require('multer');
const {storage} = require('../cloudinary'); //node automatically looks for an index.js in a folder
const upload = multer({ storage })



router.get('/', catchAsync(campgrounds.index));

router.get('/new', isLoggedIn, campgrounds.renderNewForm);

router.post('/', isLoggedIn,  upload.array('image'), validateCampground, catchAsync(campgrounds.createCampground))
// router.post('/', upload.array('image'),(req, res) => {
//     console.log(req.body, req.files);
//     res.send("It worked!")
// })

router.get('/:id', catchAsync(campgrounds.showCampground))

router.get('/:id/edit', isLoggedIn, isAuthor, catchAsync(campgrounds.renderEditForm))

router.put('/:id', isLoggedIn, isAuthor, upload.array('image'), validateCampground, catchAsync(campgrounds.updateCampground))

router.delete('/:id', isLoggedIn, isAuthor, catchAsync(campgrounds.deleteCampground))

module.exports = router;