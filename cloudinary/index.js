const cloudinary = require('cloudinary').v2;
const { CloudinaryStorage } = require('multer-storage-cloudinary');

//setting config in cloudinary
//basically associating your cloudinary account with this cloudinary instance
cloudinary.config({
    cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
    api_key: process.env.CLOUDINARY_KEY,
    api_secret:process.env.CLOUDINARY_SECRET
})

//instantiate an instance of cloudinary storage, need to pass in cloudinary object we just configured
const storage = new CloudinaryStorage({
    cloudinary,
    params: {
        folder: 'YelpCamp', //folder in cloudinary we're gonna store our files in
        allowedFormats: ['jpeg', 'png', 'jpg']
    }
});

//cloudinary storage is set up so that it has the credentials for our account
module.exports = {
    cloudinary,
    storage
}