import { Routes, Route } from 'react-router';
import Layout from '@/components/layout/Layout';
import Home from '@/pages/Home';
import ContentPage from '@/pages/ContentPage';
import SectionHub from '@/pages/SectionHub';
import FormPage from '@/pages/FormPage';
import { NewsList, NewsArticle } from '@/pages/News';

export default function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/news" element={<NewsList />} />
        <Route path="/news/:slug" element={<NewsArticle />} />
        <Route path="/academics" element={<SectionHub section="academics" />} />
        <Route path="/programs" element={<SectionHub section="programs" />} />
        <Route path="/contact" element={<FormPage type="contact" route="/contact" titleKey="forms.contactTitle" />} />
        <Route path="/book-appointment" element={<FormPage type="appointment" route="/book-appointment" titleKey="forms.bookTitle" />} />
        <Route path="/apply" element={<FormPage type="consultation" route="/apply" titleKey="forms.applyTitle" />} />
        <Route path="/admissions/enrollment" element={<FormPage type="enrollment" route="/admissions/enrollment" titleKey="forms.enrollTitle" />} />
        {/* All remaining content pages resolve through the on-demand content index */}
        <Route path="*" element={<ContentPage />} />
      </Routes>
    </Layout>
  );
}
