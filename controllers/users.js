const User = require('../models/user2');

module.exports.renderRegisterForm = (req, res)=> {
    res.render('users/register');
}

module.exports.register = async(req, res, next)=> {
    try{
        const {email, username, password} = req.body;
        const user = new User({email, username});
        const registerdUser = await User.register(user, password);
        req.login(registerdUser, err =>{
            if(err) return next(err);
            req.flash('success', 'Welcome to YelpCamp!');
            res.redirect('/campgrounds');
        })
    } catch(e){
        req.flash('error', e.message);
        res.redirect('register')
    }
}

module.exports.renderLoginForm = (req, res)=> {
    res.render('users/login');
}

module.exports.login = (req, res) => {
    req.flash('success', 'Welcome back!');
    const redirectUrl = req.session.returnTo || '/campgrounds';
    delete req.session.returnTo;
    res.redirect(redirectUrl);
}

module.exports.logout = function(req, res, next) {
    req.logout(function(err) {
      if (err) { return next(err); }
      req.flash("success", "GOOD BYE!!");
      res.redirect('/campgrounds');
    });
}