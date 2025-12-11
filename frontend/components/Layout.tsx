import Navbar from "./Navbar";

export default function Layout({ children }: any) {
  return (
    <>
      <Navbar />
      <main className="max-w-4xl mx-auto p-6 pt-24">
        {children}
      </main>
    </>
  );
}