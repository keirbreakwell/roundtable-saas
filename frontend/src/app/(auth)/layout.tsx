"use client"

import { useAuth } from "@/contexts/auth-context"
import { redirect } from 'next/navigation'
import { PropsWithChildren, useEffect } from "react"
import { Button } from "@/components/ui/button"

export default function AuthLayout({ children }: PropsWithChildren) {
  const { user, isLoading, logout } = useAuth()

  useEffect(() => {
    if (!user && !isLoading) {
      redirect('/login')
    }
  }, [user, isLoading])

  // Don't render anything until we check auth
  if (isLoading) {
    return <div>Loading...</div>
  }

  // If no user, don't render children
  if (!user) {
    return null
  }

  return (
    <div className="min-h-screen flex">
      {/* Sidebar */}
      <div className="w-64 bg-gray-100 p-4">
        <div className="text-xl font-bold mb-8">Roundtable</div>
        <nav className="space-y-2">
          <a href="/dashboard" className="block p-2 hover:bg-gray-200 rounded">Dashboard</a>
          <a href="/settings" className="block p-2 hover:bg-gray-200 rounded">Settings</a>
          <Button 
            variant="ghost" 
            className="w-full text-left mt-4"
            onClick={logout}
          >
            Logout
          </Button>
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-8">
        {children}
      </div>
    </div>
  )
}