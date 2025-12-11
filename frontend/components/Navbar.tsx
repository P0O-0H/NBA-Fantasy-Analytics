import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="fixed top-0 w-full bg-white border-b shadow-sm z-50">
      <div className="max-w-4xl mx-auto flex justify-between items-center p-4">
        <Link href="/" className="text-xl font-bold text-purple-600">
          FantasyAI
        </Link>

        <div className="flex gap-6 text-gray-700">
          <Link href="/">Home</Link>
          <Link href="/waiver">Waiver</Link>
        </div>
      </div>
    </nav>
  );
}