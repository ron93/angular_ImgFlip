import { ImgflipPage } from './app.po';

describe('imgflip App', function() {
  let page: ImgflipPage;

  beforeEach(() => {
    page = new ImgflipPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
