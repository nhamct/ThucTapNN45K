import React from "react";

import "./footer.scss";

import { Link } from "react-router-dom";

import bg from "../../assets/footer-bg.jpg";
import logo from "../../assets/tmovie.png";

const Footer = () => {
  return (
    <div className="footer" style={{ backgroundImage: `url(${bg})` }}>
      <div className="footer__content container">
        <div className="footer__content__logo">
          <div className="logo">
            <img src={logo} alt="" />
            <Link to="/">nMovies</Link>
          </div>
        </div>
        <div className="footer__content__menus">
          <div className="footer__content__menu">
            <Link to="/">Trang chủ</Link>
            <Link to="/">Phim lẻ</Link>
            <Link to="/">Phim bộ</Link>
            <Link to="/">Phim hot</Link>
          </div>
          <div className="footer__content__menu">
            <Link to="/">Phim Hàn</Link>
            <Link to="/">Phim Trung</Link>
            <Link to="/">Phim Mỹ</Link>
            <Link to="/">Phim Việt</Link>
          </div>
          <div className="footer__content__menu">
            <Link to="/">Top phim lẻ</Link>
            <Link to="/">Top phim bộ</Link>
            <Link to="/">Top Phim Việt</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
