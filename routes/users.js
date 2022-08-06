const express = require('express');
const router = express.Router();
const User = require('../models/user2');
const catchAsync = require('../utils/catchAsync');
const passport = require('passport');
const users = require('../controllers/users')


router.get('/register', users.renderRegisterForm)

router.post('/register', catchAsync(users.register))

router.get('/login', users.renderLoginForm)

router.post('/login', passport.authenticate('local',{failureFlash: true, failureRedirect:'/login', failureMessage: true, keepSessionInfo: true}), users.login)


router.get('/logout', users.logout);

module.exports = router;