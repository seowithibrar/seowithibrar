import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";

const inter = Inter({ subsets: ["latin"], variable: "--font-family" });

export const metadata = {
  title: "Best SEO Expert in Pakistan | SEO With Ibrar",
  description: "Ibrar Ahmad is the top SEO expert in Pakistan offering proven, data-driven organic growth, technical SEO, and custom WordPress development.",
  openGraph: {
    title: "Best SEO Expert in Pakistan | SEO With Ibrar",
    description: "Ibrar Ahmad is the top SEO expert in Pakistan offering proven, data-driven organic growth, technical SEO, and custom WordPress development.",
    url: "https://seowithibrar.com/",
    siteName: "SEO With Ibrar",
    images: [
      {
        url: "/images/logo-full.png",
        width: 1200,
        height: 630,
        alt: "SEO With Ibrar",
      },
    ],
    locale: "en_US",
    type: "website",
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body>
        <Navbar />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
