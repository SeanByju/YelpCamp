const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const passportLocalMongoose = require('passport-local-mongoose');

const UserSchema = new Schema({
    email: {
        type: String,
        required: true,
        unique: true,
    }
});
UserSchema.plugin(passportLocalMongoose); //will add on username and password fields to our schema

module.exports = mongoose.model('User', UserSchema);