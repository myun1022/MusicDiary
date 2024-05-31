import { useState } from 'react';
import back from './assets/background.svg';
import modal from './assets/1.svg';
import modal2 from './assets/2.svg';
import modal3 from './assets/3.svg';
import styled from 'styled-components';

import './App.css';

const Body = styled.div`
  display: flex;
  width: 100%;
  height: 100%;
`;
const TitleContainer = styled.div``;
const Title = styled.h1`
  width: 100%;
  height: 202px;
  margin: 179px 149px 20px 98px;

  color: #a99bef;
  font-family: Caveat;
  font-size: 80px;
  font-weight: bold;
`;
const Sub = styled.p`
  height: 25px;
  margin: 0 0 0 117px;
  color: #9e8aff;
  font-family: AppleSDGothicNeo;
  font-size: 22px;
  font-weight: 600;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: normal;
`;
const Button = styled.button`
  width: 301px;
  height: 68px;
  flex-grow: 0;
  margin: 349px 239px 153px 92px;
  border-radius: 19px;
  background-color: #a99bef;
  border: none;
  color: #ffffff;
  font-size: 28px;
`;
const Img = styled.img``;
const Img2 = styled.img``;
const Img3 = styled.img``;
const Img4 = styled.img``;

function App() {
  return (
    <>
      <Body>
        <TitleContainer>
          <Title>
            music? diary? <br />
            IT's life!
          </Title>
          <Sub>이제 심심한 블로그 일기는 그만! 자신의 일기에 자신감을!</Sub>
          <Button>START</Button>
        </TitleContainer>
        {/* 
        <Img src={back} alt="" />
        <Img2 src={modal} alt=""></Img2>
        <Img3 src={modal2}></Img3>
        <Img4 src={modal3}></Img4> */}
      </Body>
    </>
  );
}

export default App;
